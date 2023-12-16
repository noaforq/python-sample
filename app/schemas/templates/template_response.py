from pydantic import Field

from app.schemas.base import PydanticModel


class JobPosition(PydanticModel):
    job_position_id: int = Field(None, ge=0, description="対応する求人ID")
    job_position_name: str = Field(None, description="対応する求人名")


class TemplateResponse(PydanticModel):
    template_id: int = Field(..., description="求人ポジション名")
    template_name: str = Field(..., description="テンプレート名")
    template_subject: str = Field(..., description="件名")
    job_positions: list[JobPosition] | None
    template_body: str = Field(..., description="本文")
