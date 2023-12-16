from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import Job
    from app.models.masters import MasterProgrammingLanguage

from app.models.base.transaction_base import TransactionBase


class ProgrammingLanguage(TransactionBase):
    """求人：プログラミング言語"""

    __tablename__ = "programming_languages"

    job_id: Mapped[str] = mapped_column(sa.ForeignKey("jobs.id"), comment="求人ID")
    m_programming_language_id: Mapped[int] = mapped_column(sa.Integer(), comment="プログラミング言語ID")

    # relation
    job: Mapped["Job"] = relationship(back_populates="programming_languages")
    m_programming_language: Mapped["MasterProgrammingLanguage"] = relationship(back_populates="programming_languages")
