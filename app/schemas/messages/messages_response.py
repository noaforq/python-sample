# メッセージ左ペイン用
from datetime import datetime

from pydantic import Field

from app.schemas.base import PydanticModel


class MessageResponse(PydanticModel):
    id: str = Field(..., description="選考ID")
    icon: str = Field(..., description="ユーザーアイコン画像URL")
    account_name: str = Field(..., description="ユーザー表示名")
    real_name: str = Field(..., description="ユーザー本名（スカウト未承諾時は空文字）")
    unread_count: int = Field(..., description="未読数")
    last_send_time: datetime = Field(..., description="最終更新日時")
    is_deleted_account: bool = Field(..., description="退会アカウントか")
    is_scout_refusal_account: bool = Field(..., description="スカウト拒否アカウントか")
    is_scout_agreed: bool = Field(..., description="スカウト承諾しているか")


class MessageSelectionsResponse(PydanticModel):
    total_count: int = Field(None, description="総件数")
    selections: list[MessageResponse]
