from app.choices.base import BaseIntEnum


class CompanyDocumentType(BaseIntEnum):
    """
    企業情報資料タイプ
    """

    TEXT = 1, "テキスト"
    PDF = 2, "PDF"
    VIDEO = 3, "動画"
