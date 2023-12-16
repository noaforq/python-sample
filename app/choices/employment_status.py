from app.choices.base import BaseIntEnum


class EmploymentStatus(BaseIntEnum):
    """
    雇用形態
    """

    is_new_graduate: bool

    FULL_TIME = 1, "正社員", False
    INTERN = 2, "インターン", True
    PART_TIMER = 3, "アルバイト･パート", False
    NEW_GRADUATE = 4, "新卒", True
    CONTRACT_EMPLOYEE = 5, "契約社員", False
    SUBCONTRACTING = 6, "業務委託", False
    TEMPORARY_EMPLOYEE = 7, "嘱託社員", False

    def __new__(cls, value: int, label: str = "", is_new_graduate: bool = False) -> "EmploymentStatus":
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.label = label
        obj.is_new_graduate = is_new_graduate
        return obj

    @classmethod
    def choices(cls) -> list[dict]:
        return [{"value": m.value, "label": m.label, "is_new_graduate": m.is_new_graduate} for m in cls]
