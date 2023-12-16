from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.templates.templates_template_id_response import TemplatesTemplateIdResponse

router = APIRouter()


@router.get(
    "/{template_id}",
    response_model=TemplatesTemplateIdResponse,
    summary="テンプレート取得（特定）",
)
async def get_templates_template_id(
    template_id: int = Path(..., description="テンプレートID"),
    session: AsyncSession = Depends(get_session),
) -> TemplatesTemplateIdResponse:
    """特定のテンプレートを取得する"""

    return {
        "use_case": 1,
        "template_name": "string",
        "template_subject": "string",
        "jobs_position": [
            {"jobs_position_id": 1, "jobs_position_name": "string"},
            {"jobs_position_id": 2, "jobs_position_name": "string2"},
        ],
        "template_body": "string",
    }
