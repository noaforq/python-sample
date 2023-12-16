from app.choices.base import BaseIntEnum


class SelectionType(BaseIntEnum):
    """
    選考タイプ
    """

    SELF = 1, "自己応募"
    SCOUT = 2, "スカウト"
