from app.choices.base import BaseIntEnum


class EvaluationFunction(BaseIntEnum):
    """
    評価関数種類
    """

    ACCURACY = 1, "正解率"
    ALLOWABLE_ERROR = 2, "許容誤差(絶対誤差)"
    ALLOWABLE_ERROR_PERCENT = 3, "許容誤差(相対誤差)"
