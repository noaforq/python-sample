from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session
from app.schemas.messages.message_tempfiles_selection_id_response import MessageTempfileResponse

router = APIRouter()


@router.get(
    "/tempfiles/{selection_id}",
    response_model=list[MessageTempfileResponse],
    summary="添付ファイル取得",
)
async def post_message_selection_id(
    selection_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
) -> list[MessageTempfileResponse]:
    """ファイルの一覧を取得する"""
    # sql_query = select(Occupations).order_by(Occupations.id)
    # return (await session.scalars(sql_query)).all()

    return [
        MessageTempfileResponse(
            message_tempfile_id="abc",
            message_id="abc",
            created_at="2019-08-24T14:15:22Z",
            file_name="string",
            file="string",
            expires_at="2019-08-24T14:15:22Z",
            sender="string",
            icon="string",
        )
    ]
