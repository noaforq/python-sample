from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.templates.templates_pages_response import TemplatePageResponse

router = APIRouter()


@router.get(
    "/pages/{page}",
    response_model=TemplatePageResponse,
    summary="テンプレート取得",
)
async def get_templates_pages(
    page: int = Path(..., description="リクエストページ番号"),
    session: AsyncSession = Depends(get_session),
) -> TemplatePageResponse:
    """テンプレートの一覧を取得する（指定のページ）"""

    return {
        "total_page": 3,
        "current_page": page,
        "templates_data": [
            {
                "use_case": 1,
                "template_id": 1,
                "template_name": "string",
                "jobs_position_name": "string",
                "template_subject": "string",
                "template_body": "string",
                "update_at": "2019-08-24",
            },
            {
                "use_case": 2,
                "template_id": 2,
                "template_name": "string2",
                "jobs_position_name": "string2",
                "template_subject": "string2",
                "template_body": "string2",
                "update_at": "2019-08-24",
            },
            {
                "use_case": 1,
                "template_id": 3,
                "template_name": "string3",
                "jobs_position_name": "string3",
                "template_subject": "string3",
                "template_body": "string3",
                "update_at": "2019-08-24",
            },
            {
                "use_case": 2,
                "template_id": 4,
                "template_name": "string4",
                "jobs_position_name": "string4",
                "template_subject": "string4",
                "template_body": "string4",
                "update_at": "2019-08-24",
            },
            {
                "use_case": 1,
                "template_id": 5,
                "template_name": "string5",
                "jobs_position_name": "string5",
                "template_subject": "string5",
                "template_body": "string5",
                "update_at": "2019-08-24",
            },
        ],
    }
