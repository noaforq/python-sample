from __future__ import absolute_import, division, print_function

from typing import Any, Type

from sqlalchemy import Integer
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.types import TypeDecorator

from app.choices.base import BaseIntEnum


class IntEnum(TypeDecorator):
    """
    Enables passing in a Python enum and storing the enum's *value* in the db.
    The default would have stored the enum's *name* (ie the string).
    """

    impl = Integer
    cache_ok = True

    def __init__(self, enumtype: Type[BaseIntEnum] = BaseIntEnum, *args: Any, **kwargs: Any) -> None:
        super(IntEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value: Any, dialect: Dialect) -> int | None:
        if isinstance(value, int):
            return value
        if not value:
            return None

        return value.value

    def process_result_value(self, value: Any | None, dialect: Dialect) -> Any:
        if value is None:
            return None
        return self._enumtype(value)
