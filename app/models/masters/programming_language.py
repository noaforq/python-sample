from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.master_base import MasterBase

if TYPE_CHECKING:
    from app.models import ProgrammingLanguage


class MasterProgrammingLanguage(MasterBase):
    """プログラミング言語"""

    __tablename__ = "m_programming_languages"

    value: Mapped[str] = mapped_column(sa.String(63), comment="プログラミング言語")

    programming_languages: Mapped[list["ProgrammingLanguage"]] = relationship(back_populates="m_programming_language")
