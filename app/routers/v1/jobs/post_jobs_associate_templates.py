from fastapi import APIRouter, Depends, Path
from pydantic import Field

from app.db import AsyncSession, get_session
from app.schemas.base import PydanticModel
from app.schemas.jobs.post_jobs_associate_template_response import PostJobsAssociateTemplateResponse, TemplateData

router = APIRouter()


class TemplateIds(PydanticModel):
    template_ids: list[int] = Field(..., description="テンプレートID")


@router.post(
    "/associate_templates/{job_id}",
    summary="スカウト求人テンプレート紐づけ",
    response_model=PostJobsAssociateTemplateResponse
    # responses=error_response(ValidationError),
)
async def post_jobs_associate_templates(
    template_data_list: TemplateIds | None = None,
    job_id: int = Path(..., description="求人ID"),
    session: AsyncSession = Depends(get_session),
) -> PostJobsAssociateTemplateResponse:
    """スカウト求人をテンプレートに紐づけする"""
    # ロジック部分は後ほど記述

    result = PostJobsAssociateTemplateResponse()
    if not job_id:
        # TODO: エラー処理にする
        pass

    template_list = [TemplateData(template_id=template, template_name="string") for template in template_data_list.template_ids]

    result.template_data = template_list

    return result
