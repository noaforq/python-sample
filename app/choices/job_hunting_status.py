from app.choices.base import BaseIntEnum


class JobHuntingStatus(BaseIntEnum):
    """
    就職活動状況
    """

    NOT_DOING = 1, "就活はしていない"
    STARTING = 2, "就活の準備を始めている"
    DOING = 3, "就活中・内定を持っていない"
    HAVING_JOB_OFFER_BUT_DOING = 4, "就活中・内定を得ているが他の企業も検討したい"
    FINISHED = 5, "就職活動を終了している"
