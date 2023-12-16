from app.choices.base import BaseIntEnum


class RankingType(BaseIntEnum):
    """
    一般ユーザーのダッシュボードに表示するランキング区分
    """

    ALL = 1, "総合ランキング"
    WEEK_SCORE = 2, "週間ランキング(スコア別)"
    WEEK_ANSWER = 3, "週間ランキング(解答別)"
