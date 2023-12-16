from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.messages.message_selection_id_response import MessagesResponse, TempfileResponse

router = APIRouter()


@router.post(
    "/{selection_id}",
    response_model=MessagesResponse,
    status_code=201,
    summary="メッセージ、ファイル登録",
)
async def post_messages_selection_id(
    selection_id: str = Path(...),
    # post_message: PostMessageRequest,
    session: AsyncSession = Depends(get_session),
) -> MessagesResponse:
    """メッセージorファイルを送信する"""
    # sql_query = select(Occupations).order_by(Occupations.id)
    # return (await session.scalars(sql_query)).all()

    return MessagesResponse(
        id="hoge",
        created_at="2019-08-24T14:15:22Z",
        message_type=1,
        message="string",
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
    )
