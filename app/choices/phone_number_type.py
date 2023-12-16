from app.choices.base import BaseIntEnum


class PhoneNumberType(BaseIntEnum):
    """
    電話番号タイプ
    """

    MOBILE = 1, "携帯"
    HOME = 2, "自宅"
