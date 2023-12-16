from app.choices.base import BaseIntEnum


class EmploymentManagementStatus(BaseIntEnum):
    """
    企業における雇用管理に関する状況
    """

    PAID_HOLIDAY = 1, "前年度の有給休暇の平均取得日数"
    CHILDCARE_LEAVE = 2, "前年度の育児休業取得対象者数・取得者数（男女別）"
    PERCENTAGE_OF_WOMEN = 3, "役員に占める女性の割合及び管理的地位にある者に占める女性の割合"
