from app.choices.base import BaseIntEnum


class ContactType(BaseIntEnum):
    """
    お問い合わせタイプ
    """

    GENERAL = 1, "一般お問い合わせ"
    COMPANY = 2, "企業お問い合わせ"
    SCHOOL = 3, "学校お問い合わせ"
