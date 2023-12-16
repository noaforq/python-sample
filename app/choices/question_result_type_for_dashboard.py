from app.choices.base import BaseIntEnum


class QuestionResultTypeForDashboard(BaseIntEnum):
    """
    一般ユーザーのダッシュボードの問題解答ヒートマップ取得に使用
    """

    CHALLENGE = 2, "チャレンジ"
    PRACTICE = 3, "プラクティス"
    LEARNING = 4, "ラーニング"
