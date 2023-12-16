from app.choices.base import BaseIntEnum


class ContentDivision(BaseIntEnum):
    """
    コンテンツ区分
    """

    STOCK = 1, "ストック"
    CHALLENGE = 2, "チャレンジ"
    PRACTICE = 3, "プラクティス"
    UNCATEGORIZED = 4, "未分類"
    THIRD_PARTY = 5, "第三者作成"
    TRASH = 6, "ゴミ箱"
    LEARNING = 7, "ラーニング"


class ContentOrganizationDivision(BaseIntEnum):
    """
    コンテンツ組織別区分
    """

    OFFICIAL = 1, "公式問題"
    SCHOOL_NOT_SHARED = 2, "学校問題(企業に非公開)"
    SCHOOL_SHARED = 3, "学校問題(企業に公開)"
    COMPANY = 4, "企業問題"
