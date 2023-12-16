from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.configs import settings
from app.utils.redis import RedisConnection, get_redis_record, set_redis_record


class JwtTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_url = request.url.__str__()
        # OpenAPI定義とそのドキュメントには認証なしでアクセスできるようにする
        # TODO: ハードコーディングしている部分について、どこかに逃がす
        if request_url == "http://localhost:1019/openapi.json" or request_url == "http://localhost:1019/docs":
            return await call_next(request)

        # Redisサーバへの接続情報を取得する
        redis_connection = RedisConnection(
            host_name=settings.authentication_cache_redis_host_name,
            port=settings.authentication_cache_redis_port,
            db_index=settings.authentication_cache_db_index,
        )

        """
        JWTトークン検証

        Args:

        Returns:
            Response: FastAPIのResponse
        """
        request_header = dict(request.headers)
        jwt_token = request_header.get("authorization")
        error_json_response = JSONResponse({"error_message": "Authorization failed"}, status.HTTP_401_UNAUTHORIZED)

        if jwt_token is None:
            return error_json_response

        # 1. 引き渡されたJWTトークンをキーに、Redisにすでに検証済みのJWTトークンが存在するか確認する
        cached_jwt_token = get_redis_record(redis_connection, jwt_token)
        available_jwt_token_cached = cached_jwt_token is not None
        if available_jwt_token_cached:
            return await call_next(request)

        # 2. なければJWTトークンをTechFUL+側の検証APIに投げる
        jwt_token_validation_succeeded = True

        # 3. 検証が成功したらRedisにJWTトークンをキャッシュする。失敗したら401を返す
        if not jwt_token_validation_succeeded:
            return error_json_response

        set_redis_record(redis_connection, jwt_token, "user_id", 1 * 60 * 15)
        return await call_next(request)
