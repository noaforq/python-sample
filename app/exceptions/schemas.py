from pydantic import Field

from app.schemas.base import PydanticModel


class ApiError(PydanticModel):
    error_code: str
    message: str
    detail: str


class ValidationErrorDetail(PydanticModel):
    loc: list[str | int]
    msg: str
    type: str


class ValidationError(PydanticModel):
    error_code: str = Field(..., example="VALIDATION_ERROR")
    message: str = Field(..., example="入力値が不正です")
    detail: list[ValidationErrorDetail]
