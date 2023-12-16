from fastapi import APIRouter, Depends, Path

from app.db import AsyncSession, get_session

router = APIRouter()


@router.delete(
    "/tempfiles/{message_tempfile_id}",
    status_code=204,
    summary="ファイル削除",
)
async def delete_messages_tempfiles_message_tempfile_id(
    message_tempfile_id: str = Path(...),
    session: AsyncSession = Depends(get_session),
) -> None:
    """ファイルを削除する"""
    # sql_query = select(Occupations).order_by(Occupations.id)
    # return (await session.scalars(sql_query)).all()
