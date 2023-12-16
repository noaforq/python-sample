from app.choices.base import BaseIntEnum


class Probation(BaseIntEnum):
    """
    求人試用期間
    """

    NOTHING = 0, "なし"
    ONE_MONTH = 1, "1ヶ月"
    TWO_MONTH = 2, "2ヶ月"
    THREE_MONTH = 3, "3ヶ月"
    FOUR_MONTH = 4, "4ヶ月"
    FIVE_MONTH = 5, "5ヶ月"
    SIX_MONTH = 6, "6ヶ月"
