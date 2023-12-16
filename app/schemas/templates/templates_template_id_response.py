from pydantic import Field

from app.schemas.base import PydanticModel


class JobPosition(PydanticModel):
    jobs_position_id: int = Field(None, ge=0, description="対応する求人ID")
    jobs_position_name: str = Field(None, description="対応する求人名")


class TemplatesTemplateIdResponse(PydanticModel):
    use_case: int = Field(..., ge=1, description="用途")
    template_name: str = Field(..., description="テンプレート名")
    template_subject: str = Field(..., description="件名")
    jobs_position: list[JobPosition] | None
    template_body: str = Field(..., description="本文")
