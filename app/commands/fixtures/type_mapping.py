from datetime import date, datetime

from app.choices.base import BaseIntEnum
from app.choices.techful_school_division import TechFulSchoolDivision


def get_type_mapping() -> dict:
    """modelのpython_type: 変換関数"""
    return {
        str: str,
        int: to_int,
        float: to_float,
        bool: to_bool,
        datetime: to_datetime,
        date: to_date,
        TechFulSchoolDivision: to_techful_school_div,
    }


def to_int(int_str: str) -> int | None:
    if int_str == "":
        return None
    else:
        return int(int_str)


def to_float(float_str: str) -> float | None:
    if float_str == "":
        return None
    else:
        return float(float_str)


def to_bool(bool_str: str) -> bool | None:
    if bool_str == "True" or bool_str == "true":
        return True
    elif bool_str == "False" or bool_str == "false":
        return False
    elif bool_str == "":
        return None
    else:
        raise ValueError("unexpected bool string.")


def to_datetime(datetime_str: str) -> datetime | None:
    if datetime_str == "":
        return None
    else:
        return datetime.fromisoformat(datetime_str)


def to_date(date_str: str) -> date | None:
    if date_str == "":
        return None
    else:
        return date.fromisoformat(date_str)


def to_techful_school_div(div: str) -> BaseIntEnum | None:
    if div == "":
        return None
    else:
        return TechFulSchoolDivision.__new__(TechFulSchoolDivision, int(div))
