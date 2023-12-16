from fastapi import APIRouter, Depends

from app.db import AsyncSession, get_session
from app.schemas.reactions.reactions_response import (
    ReactionsResponse,
    ReactionsResponseJob,
    ReactionsResponseReactionsReport,
    ReactionsResponseScout,
)

router = APIRouter()


@router.get("", response_model=ReactionsResponse, summary="効果測定取得")
async def get_reactions(session: AsyncSession = Depends(get_session)) -> ReactionsResponse:
    return ReactionsResponse(
        reactions_reports=[
            ReactionsResponseReactionsReport(
                scout=ReactionsResponseScout(
                    send_count=0,
                    opened_count=0,
                    opened_rate=0.0,
                    agreed_count=0,
                    agreed_rate=0.0,
                    replied_count=0,
                    replied_rate=0.0,
                ),
                job=ReactionsResponseJob(viewed_count=0, applied_count=0, applied_rate=0.0),
                start_date="2023-10-19T00:00:00Z",
                position_name="Test",
            )
        ]
    )
