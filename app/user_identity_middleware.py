import base64
import json

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.configs import settings
from app.utils.redis import RedisConnection, get_redis_record, set_redis_record


class UserIdentityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        redis_connection = RedisConnection(
            host_name=settings.user_identity_cache_redis_host_name,
            port=settings.user_identity_cache_redis_port,
            db_index=settings.user_identity_cache_db_index,
        )

        request_header = dict(request.headers)
        error_json_response = JSONResponse({"error_message": "Authorization failed"}, status.HTTP_401_UNAUTHORIZED)

        authorization_header = request_header.get("authorization")
        if authorization_header is None:
            return error_json_response

        # 1. Authorizationヘッダに顕現するJWTトークンの中から
        # ユーザ情報を含むペイロード部分を取得する
        payload = request_header.get("authorization")
        if payload is None:
            return error_json_response

        payload_content = payload.split(".")[1]
        encoded_payload = json.loads(base64.b64decode(payload_content + "=" * (-len(payload_content) % 4)).decode())

        # 2. Redisにユーザ情報のキャッシュを見に行く
        redis_connection = RedisConnection(
            host_name=settings.user_identity_cache_redis_host_name,
            port=settings.user_identity_cache_redis_port,
            db_index=settings.user_identity_cache_db_index,
        )

        identity_existence_verifying_user_id = encoded_payload["user_id"]
        user_exists = get_redis_record(redis_connection, identity_existence_verifying_user_id) is not None
        if user_exists:
            return await call_next(request)

        # 3. Redisになければユーザ情報を見に行く
        # TODO: companies テーブルができてないので常に存在していることにする
        set_redis_record(redis_connection, identity_existence_verifying_user_id, payload_content, 1 * 60 * 15)

        # TODO: Redisにない場合は401を返す
        # return error_json_response

        return await call_next(request)
