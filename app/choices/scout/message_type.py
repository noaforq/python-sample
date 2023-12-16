from app.choices.base import BaseIntEnum


class MessageType(BaseIntEnum):
    """
    メッセージタイプ
    """

    SCOUT = 1, "メッセージ"
    SELF = 2, "ファイル"
