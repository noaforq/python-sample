from app.choices.base import BaseIntEnum


class CompanyPlanStatusNoTrial(BaseIntEnum):
    """
    企業プラン加入状況(トライアルなし)
    """

    NOT_SUBSCRIBED = 1, "未加入"
    SUBSCRIBED = 3, "本申込"
