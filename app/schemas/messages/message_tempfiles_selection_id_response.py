# ファイル一覧用
from datetime import datetime

from pydantic import Field

from app.schemas.base import PydanticModel


class MessageTempfileResponse(PydanticModel):
    message_tempfile_id: str = Field(..., description="ファイルID")
    message_id: str = Field(..., description="メッセージID")
    created_at: datetime = Field(..., description="作成日時")
    file_name: str = Field(..., description="ファイル名")
    file: str = Field(..., description="ファイルURL")
    expires_at: datetime = Field(..., description="有効期限")
    sender: str = Field(..., description="送信者名")
    icon: str = Field(..., description="アイコンURL")
