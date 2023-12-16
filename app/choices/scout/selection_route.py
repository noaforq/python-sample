from app.choices.base import BaseIntEnum


class SelectionRoute(BaseIntEnum):
    """
    選考管理/スカウト経由（スカウト非公開求人） or 公開求人経由（スカウト公開求人）
    """

    SCOUT = 1, "スカウト"
    SELF = 2, "応募"
