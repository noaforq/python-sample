from app.choices.base import BaseIntEnum


class JobChangingStatus(BaseIntEnum):
    """
    転職活動状況
    """

    NOT_THINKING = 1, "転職は考えていない"
    THINKING = 2, "自分にあった求人であれば転職を考えたい"
    DOING = 3, "転職活動をしている"
