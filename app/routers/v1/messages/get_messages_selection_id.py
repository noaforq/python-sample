from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.messages.message_selection_id_response import (
    MessagesResponse,
    MessageTimelineResponse,
    TempfileResponse,
)

router = APIRouter()


@router.get(
    "/{selection_id}",
    response_model=MessageTimelineResponse,
    summary="メッセージ取得（個別）",
)
async def get_message_selection_id(
    selection_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
) -> MessageTimelineResponse:
    """メッセージタイムラインに表示するメッセージとファイルの一覧を取得する"""
    # sql_query = select(Occupations).order_by(Occupations.id)
    # return (await session.scalars(sql_query)).all()

    return MessageTimelineResponse(
        icon="string",
        account_name=selection_id,
        real_name=selection_id,
        is_deleted_account=True,
        is_scout_refusal_account=True,
        is_scout_agreed=True,
        messages=[
            MessagesResponse(
                id="hoge",
                created_at="2019-08-24T14:15:22Z",
                message_type=1,
                message="string",
                is_read=True,
                is_own=True,
                sender="string",
                icon="string",
            ),
            MessagesResponse(
                id="huga",
                created_at="2019-08-24T14:15:22Z",
                message_type=2,
                message="",
                is_read=True,
                is_own=True,
                sender="string",
                icon="string",
                file=TempfileResponse(
                    file_name="string",
                    file="string",
                    expires_at="2019-08-24T14:15:22Z",
                    is_expired=True,
                    is_disable=True,
                ),
            ),
        ],
    )
