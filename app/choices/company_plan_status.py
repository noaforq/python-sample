from app.choices.base import BaseIntEnum


class CompanyPlanStatus(BaseIntEnum):
    """
    企業プラン加入状況
    """

    NOT_SUBSCRIBED = 1, "未加入"
    TRIAL = 2, "トライアル"
    SUBSCRIBED = 3, "本申込"
