from datetime import datetime

from pydantic import Field

from app.schemas.base import PydanticModel


class JobsData(PydanticModel):
    job_title: str = Field(..., description="ポジション名")
    graduation_year: int = Field(None, description="対象卒業年度")
    employment_status: int = Field(..., ge=1, description="雇用形態")
    skill_level: int = Field(None, ge=0, description="スキルレベル")
    status: int = Field(..., ge=0, description="求人の状態")
    created_at: datetime = Field(..., description="作成日")
    updated_at: datetime = Field(..., description="更新日")


class GetJobsResponse(PydanticModel):
    todal_page: int = Field(..., ge=1, description="総ページ数")
    current_page: int = Field(..., ge=1, description="現在ページ番号")
    jobs_data: list[JobsData] | None
