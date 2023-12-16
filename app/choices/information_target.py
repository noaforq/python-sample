from app.choices.base import BaseIntEnum


class InformationTarget(BaseIntEnum):
    """
    お知らせ表示対象
    """

    ALL = 1, "全ユーザ"
    COMPANY_SCOUT_PLAN = 2, "企業採用担当（人材紹介・スカウト）"
    COMPANY_SKILL_RATING_PLAN = 3, "企業社内育成（スキル評価）"
    SCHOOL_ADMIN = 4, "学校管理者"
    USER = 5, "ユーザー"
    COMPANY = 6, "企業"
