from fastapi import APIRouter, Depends

from app.db import AsyncSession, get_session
from app.schemas.messages.messages_response import MessageResponse, MessageSelectionsResponse

router = APIRouter()


@router.get(
    "",
    response_model=MessageSelectionsResponse,
    summary="メッセージ取得",
)
async def get_sample(
    session: AsyncSession = Depends(get_session),
) -> MessageSelectionsResponse:
    """選考一覧（メッセージ用）を取得する"""
    # sql_query = select(Occupations).order_by(Occupations.id)
    # return (await session.scalars(sql_query)).all()

    return MessageSelectionsResponse(
        total_count=1,
        selections=[
            MessageResponse(
                id="hoge",
                icon="string",
                account_name="string",
                real_name="string",
                unread_count=0,
                last_send_time="2019-08-24T14:15:22Z",
                is_deleted_account=False,
                is_scout_refusal_account=False,
                is_scout_agreed=True,
            )
        ],
    )
