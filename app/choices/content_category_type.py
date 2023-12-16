from app.choices.base import BaseIntEnum


class ContentCategoryType(BaseIntEnum):
    """
    コンテンツカテゴリタイプ
    """

    GENERAL = 1, "一般問題・教材"
    PRO = 2, "PRO問題"
    TECHTHON = 3, "テックソン"
