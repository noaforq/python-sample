from collections import defaultdict
from typing import Type

from app.exceptions.exceptions import BaseAPIException
from app.exceptions.schemas import ApiError


def error_response(*exceptions: Type[BaseAPIException]) -> dict:
    """APIExceptionからopenapiのresponsesを生成

    使用方法
    @router.get(
        "/api/example",
        responses=error_response([APIError1, APIError2])
    )
    """
    exception_map: dict[int, list[Type[BaseAPIException]]] = defaultdict(list)
    for exc in exceptions:
        exception_map[exc.status_code].append(exc)
    return {
        status_code: {
            "description": "<br>".join([f"{exc.__doc__}: {exc.error_code}" for exc in exc_list]),
            "model": ApiError,
            "content": {
                "application/json": {
                    "examples": {
                        exc.error_code: {
                            "value": {
                                "errorCode": exc.error_code,
                                "message": exc.default_message,
                                "detail": exc.default_detail,
                            }
                        }
                        for exc in exc_list
                    },
                }
            },
        }
        for status_code, exc_list in exception_map.items()
    }
