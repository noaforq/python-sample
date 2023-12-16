from enum import Enum
from typing import Any


class BaseOrderingEnum(str, Enum):
    ordering: Any

    def __new__(cls, value: object, ordering: Any) -> "BaseOrderingEnum":
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.ordering = ordering
        return obj
