from app.choices.base import BaseIntEnum


class JobHuntingType(BaseIntEnum):
    """
    求職ステータス
    """

    JOB_HUNTING = 1, "就職したい"
    JOB_CHANGE = 2, "転職したい"
    PART_TIME_INTERN = 3, "アルバイト/インターン"
    OTHERS = 4, "その他"
    NEXT_STAGE_OF_EDUCATION = 5, "進学予定"
