from app.choices.base import BaseIntEnum


class TargetAudienceType(BaseIntEnum):
    """
    チュートリアル目標ユーザータイプ
    1: 一般ユーザー向け, 2: 学校ユーザー向け, 3: 企業ユーザー向け
    """

    GENERAL_USER = 1, "一般ユーザー向け"
    SCHOOL_USER = 2, "学校ユーザー向け"
    COMPANY_USER = 3, "企業ユーザー向け"
