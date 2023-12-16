from fastapi import APIRouter, Depends, Path
from pydantic import Field

from app.db import AsyncSession, get_session
from app.schemas.base import PydanticModel
from app.schemas.templates.template_update_response import JobPosition, TemplateUpdateResponse

router = APIRouter()


class TemplateData(PydanticModel):
    template_name: str = Field(..., description="テンプレート名")
    template_subject: str = Field(..., description="件名")
    job_position_ids: list[int] | None = None
    template_body: str = Field(..., description="本文")


@router.put(
    "/{template_id}",
    response_model=TemplateUpdateResponse,
    summary="テンプレート更新",
)
async def put_templates(
    template_data: TemplateData,
    template_id: int = Path(..., description="テンプレートID"),
    session: AsyncSession = Depends(get_session),
) -> TemplateUpdateResponse:
    """テンプレートを更新する"""

    job_list = []
    print(template_data.job_position_ids)
    if template_data.job_position_ids:
        for job_id in template_data.job_position_ids:
            job_position = JobPosition(job_position_id=job_id, job_position_name="string")
            job_list.append(job_position)

    result = TemplateUpdateResponse(
        template_id=1,
        template_name=template_data.template_name,
        template_subject=template_data.template_subject,
        job_positions=job_list,
        template_body=template_data.template_body,
    )

    return result
