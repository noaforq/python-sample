from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session

router = APIRouter()


@router.delete(
    "/{template_id}",
    summary="テンプレート削除",
)
async def delete_templates(
    template_id: int = Path(..., description="テンプレートID"),
    session: AsyncSession = Depends(get_session),
) -> None:
    """テンプレートを削除する"""
    return
