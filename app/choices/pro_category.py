from app.choices.base import BaseIntEnum


class ProCategory(BaseIntEnum):
    """
    PRO問題カテゴリ
    """

    IMAGE_CLASSIFICATION = 1, "画像分類"
    DATA_SCIENCE = 2, "データサイエンス"
    NATURAL_LANGUAGE_PROCESSIONG = 3, "自然言語処理"
