from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session

router = APIRouter()


@router.delete(
    "/{job_id}",
    summary="スカウト求人削除",
)
async def delete_jobs_close(
    job_id: int = Path(..., ge=1, description="求人ID"),
    session: AsyncSession = Depends(get_session),
) -> None:
    """スカウト求人を削除する"""

    if job_id is None:
        # TODO: エラー処理
        pass

    return
