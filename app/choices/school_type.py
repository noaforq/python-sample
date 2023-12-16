from app.choices.base import BaseIntEnum


class SchoolType(BaseIntEnum):
    """
    学校の種類
    """

    NATIONAL_UNIVERSITY = 1, "国立大学"
    PUBLIC_UNIVERSITY = 2, "公立大学"
    PRIVATE_UNIVERSITY = 3, "私立大学"
    TECHNICAL_SCHOOL = 4, "高専"
    TECHNICAL_COLLEGE = 5, "専門学校"
    HIGH_SCHOOL = 6, "高校"
    JUNIOR_HIGH_SCHOOL = 7, "中学校"
    ELEMENTARY_SCHOOL = 8, "小学校"
    SCHOOL = 9, "スクール"
    FOREIGN_UNIVERSITY = 10, "大学（海外）"
    FOREIGN_HIGH_SCHOOL = 11, "高校（海外）"
    FOREIGN_JUNIOR_HIGH_SCHOOL = 12, "中学校（海外）"
    VOCATIONAL_SCHOOL = 13, "職業訓練校"
    SPECIAL_NEEDS_SCHOOL = 14, "特別支援学校"
    OTHERS = 15, "その他"
    GRADUATE_SCHOOL_MASTER = 16, "大学院修士課程"
    GRADUATE_SCHOOL_DOCTOR = 17, "大学院博士課程"
