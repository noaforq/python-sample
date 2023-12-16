from app.choices.base import BaseIntEnum


class ContentPackageLevel(BaseIntEnum):
    """
    コンテンツパッケージレベル
    """

    BEGINNER = 1, "初級未達"
    ELEMENTARY = 2, "初級"
    INTERMEDIATE = 3, "中級"
    ADVANCED = 4, "上級"
    PRO = 5, "プロ"
