from app.choices.base import BaseIntEnum


class JobSelectionType(BaseIntEnum):
    """
    求人選考タイプ
    求人原稿作成に使用する
    """

    AGENT = 1, "エージェント経由"
    DIRECT = 2, "自社選考"
