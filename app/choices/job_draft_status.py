from app.choices.base import BaseIntEnum


class JobDraftStatus(BaseIntEnum):
    """
    求人下書ステータス
    """

    EDITING = 1, "編集中"
    APPLYING = 2, "申請中"
    APPROVED = 3, "承認済"
    REJECTED = 9, "却下"
