from app.choices.base import BaseIntEnum


class SchoolUserType(BaseIntEnum):
    """
    学校管理ユーザータイプ
    """

    ADMIN = 1, "管理者"
    TEACHER = 2, "先生"
