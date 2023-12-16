from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.reactions.reactions_applied_request import ReactionsAppliedRequest

router = APIRouter()


@router.post("/{job_id}/{selection_id}/applied", summary="効果測定ログ作成-応募")
async def post_reactions_applied(
    reactions_applied: ReactionsAppliedRequest,
    job_id: str = Path(..., description="求人ID"),
    selection_id: str = Path(..., description="選考ID"),
    session: AsyncSession = Depends(get_session),
) -> dict:
    return {}
