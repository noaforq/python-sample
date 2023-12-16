from app.choices.base import BaseIntEnum


class RecruitmentAndHiringStatusItem(BaseIntEnum):
    """
    募集採用に関する状況
    """

    NUM_OF_HIRES_AND_JOB_LEAVERS = 1, "過去３年間の新卒採用者数・離職者数"
    NUM_OF_HIRES_BY_GENDER = 2, "過去３年間の新卒採用者数の男女別人数"
    AVERAGE_LENGTH_OF_SERVICE = 3, "平均勤続年数"
