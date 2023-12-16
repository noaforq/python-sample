from app.choices.base import BaseIntEnum


class TechFulSchoolDivision(BaseIntEnum):
    """
    TechFul学校区分

    """

    DOCTOR = 1, "大学院(博士)"
    MASTER = 2, "大学院(修士)"
    BACHELOR = 3, "大学(学士)"
    TECHNICAL_COLLEGE = 4, "高等専門学校"
    JUNIOR_COLLEGE = 5, "短期大学"
    VOCATIONAL_SCHOOL = 6, "専門学校"
    HIGH_SCHOOL = 7, "高校"
    MIDDLE_SCHOOL = 8, "小・中学校"
    OTHER = 9, "その他"
