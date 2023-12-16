# メッセージ右ペイン用
from datetime import datetime

from pydantic import Field

from app.schemas.base import PydanticModel


class TempfileResponse(PydanticModel):
    file_name: str = Field(..., description="ファイル名")
    file: str = Field(..., description="ファイルURL")
    expires_at: datetime = Field(..., description="有効期限")
    is_expired: bool = Field(..., description="有効期限切れか")
    is_disable: bool = Field(False, description="削除済みか")


class MessagesResponse(PydanticModel):
    id: str = Field(..., description="メッセージID")
    created_at: datetime = Field(..., description="作成日時")
    message_type: int = Field(..., description="1:メッセージ, 2:ファイル")
    message: str = Field(..., description="メッセージ")
    is_read: bool = Field(..., description="既読か")
    is_own: bool = Field(..., description="自身のメッセージか")
    sender: str = Field(..., description="メッセージ送信者の名前")
    icon: str = Field(..., description="メッセージ送信者のアイコン")
    file: TempfileResponse = Field(None, description="ファイル情報（ファイルの時のみ）")


class MessageTimelineResponse(PydanticModel):
    icon: str = Field(..., description="ユーザーアイコン画像URL")
    account_name: str = Field(..., description="ユーザー表示名")
    real_name: str = Field(..., description="ユーザー本名（スカウト未承諾時は空文字）")
    is_deleted_account: bool = Field(..., description="退会アカウントか")
    is_scout_refusal_account: bool = Field(..., description="スカウト拒否アカウントか")
    is_scout_agreed: bool = Field(..., description="スカウト承諾しているか")
    messages: list[MessagesResponse] = Field(description="各メッセージ情報（メッセージがなければ空配列）")
