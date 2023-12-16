from pydantic import Field

from app.schemas.base import PydanticModel


class TemplateData(PydanticModel):
    template_id: int = Field(..., ge=1, description="テンプレートID")
    template_name: str = Field(..., description="テンプレート名")


class TemplateDataResponse(PydanticModel):
    templates_data: list[TemplateData] | None
