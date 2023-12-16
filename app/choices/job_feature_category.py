from app.choices.base import BaseIntEnum


class JobFeatureCategory(BaseIntEnum):
    """
    求人特徴カテゴリ
    """

    HOLIDAY_WORKING = 1, "休日･働き方"
    RECRUITMENT_INFO_FEATURE = 2, "採用の情報･特徴"
    TREATMENT_WELFARE = 3, "待遇･福利厚生"
    COMPANY_WORKPLACE = 4, "会社･職場"
    ENGINEER_FEATURE = 5, "エンジニア特徴"
