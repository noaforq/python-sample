from fastapi import FastAPI, Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import RequestValidationError
from starlette.responses import JSONResponse

from app.exceptions.exceptions import BaseAPIException


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(BaseAPIException)
    async def base_api_exception_handler(request: Request, exc: BaseAPIException) -> Response:
        headers = getattr(exc, "headers", None)
        if headers:
            return JSONResponse(
                {
                    "errorCode": exc.error_code,
                    "message": exc.message,
                    "detail": exc.detail,
                },
                status_code=exc.status_code,
                headers=headers,
            )
        else:
            return JSONResponse(
                {
                    "errorCode": exc.error_code,
                    "message": exc.message,
                    "detail": exc.detail,
                },
                status_code=exc.status_code,
            )

    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "errorCode": "VALIDATION_ERROR",
                "message": "入力値が不正です",
                "detail": jsonable_encoder(exc.errors()),
            },
        )

    @app.exception_handler(NotImplementedError)
    async def not_implemented_error_exception_handler(request: Request, exc: NotImplementedError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            content="未実装",
        )
