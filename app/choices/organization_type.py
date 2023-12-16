from app.choices.base import BaseIntEnum


class OrganizationType(BaseIntEnum):
    """
    組織タイプ
    """

    COMPANY = 1, "企業"
    SCHOOL = 2, "学校"
