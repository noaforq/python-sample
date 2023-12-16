from app.choices.base import BaseIntEnum


class ChatType(BaseIntEnum):
    """
    チャットタイプ
    """

    MESSAGE = 1, "メッセージ"
    FILE = 2, "ファイル"
