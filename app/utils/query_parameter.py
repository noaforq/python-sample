from enum import Enum
from typing import Any


class BaseQueryParameterEnum(str, Enum):
    parameter: Any

    def __new__(cls, value: object, parameter: Any) -> "BaseQueryParameterEnum":
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.parameter = parameter
        return obj
