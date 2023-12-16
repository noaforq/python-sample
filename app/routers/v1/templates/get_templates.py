from fastapi import APIRouter, Depends

from app.db import AsyncSession, get_session
from app.schemas.templates.template_data_response import TemplateDataResponse

router = APIRouter()


@router.get(
    "",
    response_model=TemplateDataResponse,
    summary="テンプレート選択",
)
async def get_templates(
    session: AsyncSession = Depends(get_session),
) -> TemplateDataResponse:
    """テンプレートの一覧を取得する"""

    return {
        "templates_data": [
            {"template_id": 1, "template_name": "string"},
            {"template_id": 2, "template_name": "string2"},
            {"template_id": 3, "template_name": "string3"},
        ]
    }
