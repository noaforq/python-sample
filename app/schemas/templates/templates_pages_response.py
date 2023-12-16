from pydantic import Field

from app.schemas.base import PydanticModel


class TemplateResponse(PydanticModel):
    template_id: int = Field(..., description="求人ポジション名")
    template_name: str = Field(..., description="テンプレート名")
    template_subject: str = Field(..., description="件名")
    jobs_position_name: str = Field(None, description="対応する求人名")
    template_body: str = Field(..., description="本文")


class TemplatePageResponse(PydanticModel):
    total_page: int = Field(1, description="総ページ数")
    current_page: int = Field(1, description="現在ページ番号")
    templates_data: list[TemplateResponse] | None
