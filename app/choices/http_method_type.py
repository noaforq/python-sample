from app.choices.base import BaseIntEnum


class HttpMethodType(BaseIntEnum):
    """
    HTTPメソッド種類
    """

    POST = 1, "POST"
    GET = 2, "GET"
    PUT = 3, "PUT"
    DELETE = 4, "DELETE"
