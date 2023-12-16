from app.choices.base import BaseIntEnum


class UserType(BaseIntEnum):
    """
    ユーザータイプ
    """

    GENERAL = 1, "一般ユーザー"
    SKILL_CHECK = 2, "スキルチェックユーザー"
    COMPANY = 3, "企業ユーザー"
    SCHOOL = 4, "学校ユーザー"
    RECRUITMENT = 5, "人材紹介企業ユーザー"
    STAFF = 6, "スタッフ"
    PART_TIMER = 7, "アルバイト"
    BATCH = 999, "バッチ実行ユーザー"
