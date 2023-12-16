from datetime import datetime

from app.exceptions.exceptions import ParameterError


def check_period(start: datetime, end: datetime) -> None:
    """入力された期間が365日以内か確認"""
    if (end - start).days > 365:
        raise ParameterError(detail="期間は365日以内で指定してください。")


def check_comparison(start: datetime, end: datetime) -> None:
    """入力された値がstart<=endになっているか確認"""
    if start >= end:
        raise ParameterError(detail="正しい期間を指定してください。")
