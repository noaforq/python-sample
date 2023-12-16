from fastapi import APIRouter, Depends
from pydantic import Field

from app.db import AsyncSession, get_session
from app.schemas.base import PydanticModel
from app.schemas.templates.template_response import JobPosition, TemplateResponse

router = APIRouter()


class TemplateData(PydanticModel):
    use_case: int = Field(..., ge=0, description="用途")
    template_name: str = Field(..., description="テンプレート名")
    template_subject: str = Field(..., description="件名")
    job_position_ids: list[int] | None = None
    template_body: str = Field(..., description="本文")


@router.post(
    "",
    response_model=TemplateResponse,
    summary="テンプレート作成",
)
async def post_templates(
    template_data: TemplateData,
    session: AsyncSession = Depends(get_session),
) -> TemplateResponse:
    """テンプレートを作成する"""

    job_list = []
    if template_data.job_position_ids:
        for job_id in template_data.job_position_ids:
            job_position = JobPosition(job_position_id=job_id, job_position_name="string")
            job_list.append(job_position)

    result = TemplateResponse(
        template_id=1,
        template_name=template_data.template_name,
        template_subject=template_data.template_subject,
        job_positions=job_list,
        template_body=template_data.template_body,
    )

    return result
