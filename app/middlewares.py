from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configs import settings
from app.jwttoken_middleware import JwtTokenMiddleware
from app.user_identity_middleware import UserIdentityMiddleware


def add_middlewares(app: FastAPI) -> None:
    # CORS header
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # JWTトークンを検証するミドルウェア
    # TODO: 今のところモック
    app.add_middleware(JwtTokenMiddleware)

    # ユーザの身元を確認するミドルウェア
    app.add_middleware(UserIdentityMiddleware)

    # アクセスログをとるためのミドルウェア
    # ローカルで以下の環境変数を設定しない(ローカルだとテストが通らなくなる)
    # if PROJECT_ID:
    #    app.add_middleware(AccessLogMiddleware)
