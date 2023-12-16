from fastapi import APIRouter, Depends

from app.db import AsyncSession, get_session
from app.schemas.reactions.reactions_summary_response import (
    ReactionsSummaryResponse,
    ReactionsSummaryResponseJob,
    ReactionsSummaryResponseReactionsReport,
    ReactionsSummaryResponseScout,
)

router = APIRouter()


@router.get("/summary", response_model=ReactionsSummaryResponse, summary="効果測定サマリー取得")
async def get_reactions_summary(session: AsyncSession = Depends(get_session)) -> ReactionsSummaryResponse:
    return ReactionsSummaryResponse(
        reaction_summary=ReactionsSummaryResponseReactionsReport(
            scout=ReactionsSummaryResponseScout(
                total_count=0,
                send_count=0,
                opened_count=0,
                opened_rate=0.0,
                agreed_count=0,
                agreed_rate=0.0,
                replied_count=0,
                replied_rate=0.0,
            ),
            job=ReactionsSummaryResponseJob(total_count=0, viewed_count=0, applied_count=0, applied_rate=0.0),
        )
    )
