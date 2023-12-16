from pydantic import Field

from app.schemas.base import PydanticModel


class TemplateData(PydanticModel):
    template_id: int = Field(..., description="テンプレートID")
    template_name: str = Field(..., description="テンプレート名")


class PostJobsAssociateTemplateResponse(PydanticModel):
    template_data: list[TemplateData] = Field(None, description="テンプレート情報")
