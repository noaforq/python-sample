from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session

router = APIRouter()


@router.post("/{job_id}/{selection_id}/agreed", summary="効果測定ログ作成-承認")
async def post_reactions_agreed(
    job_id: str = Path(..., description="求人ID"),
    selection_id: str = Path(..., description="選考ID"),
    session: AsyncSession = Depends(get_session),
) -> dict:
    return {}
