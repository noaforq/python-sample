from app.choices.base import BaseIntEnum


class ChatRoomType(BaseIntEnum):
    """
    チャットルームタイプ
    """

    COMPANY = 1, "企業"
    SCHOOL = 2, "学校"
    AGENT = 3, "エージェント"
