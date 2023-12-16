from app.choices.base import BaseIntEnum


class EducationalMaterialType(BaseIntEnum):
    """
    教材タイプ
    """

    TEXT = 1, "テキスト"
    PDF = 2, "PDF"
    VIDEO = 3, "動画"
