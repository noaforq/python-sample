from app.choices.base import BaseIntEnum


class CurrentJob(BaseIntEnum):
    """
    現在の職業
    """

    STUDENT = 1, "学生"
    EMPLOYEE = 2, "会社員"
    CIVIL_SERVANT = 3, "公務員"
    PART_TIMER = 4, "フリーター"
    SELF_EMPLOYED = 5, "自営業"
    OTHERS = 6, "その他"
