from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase

if TYPE_CHECKING:
    from app.models import Company, Job, ManagedStudent, Selection


class Reaction(TransactionBase):
    __tablename__ = "reactions"

    company_id: Mapped[int] = mapped_column(sa.ForeignKey("companies.company_id"), comment="企業ID")
    company: Mapped["Company"] = relationship(back_populates="reactions")
    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    job: Mapped["Job"] = relationship(back_populates="reactions")
    selections_id: Mapped[str] = mapped_column(sa.ForeignKey("selections.id", ondelete="CASCADE"))
    selection: Mapped["Selection"] = relationship(back_populates="reactions")
    student_id: Mapped[int] = mapped_column(sa.ForeignKey("managed_students.student_id", ondelete="CASCADE"), comment="学生の一意の識別子")
    managed_student: Mapped["ManagedStudent"] = relationship(back_populates="reactions")
    activity_date: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="")
    opened: Mapped[bool] = mapped_column(sa.Boolean(False), comment="")
    agreed: Mapped[bool] = mapped_column(sa.Boolean(False), comment="")
    replied: Mapped[bool] = mapped_column(sa.Boolean(False), comment="")
    viewed: Mapped[bool] = mapped_column(sa.Boolean(False), comment="")
    applied: Mapped[bool] = mapped_column(sa.Boolean(False), comment="")
