from app.choices.base import BaseIntEnum


class Status(BaseIntEnum):
    """
    求人ステータス
    """

    NONE = 0, ""
    DRAFT = 10, "下書き"
    APPLYING = 20, "申請中"
    REJECTED = 25, "差し戻し"
    APPROVED = 30, "承認済"
    PUBLISH = 40, "	掲載"
    UNPUBLISH = 50, "掲載停止"
    CLOSE = 90, "却下"
