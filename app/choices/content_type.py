from app.choices.base import BaseIntEnum


class ContentType(BaseIntEnum):
    """
    コンテンツタイプ
    """

    GENERAL = 1, "一般問題"
    PRO = 2, "PRO問題"
    TECHTHON = 3, "テックソン"
    EDUCATIONAL_MATERIAL = 4, "教材"
