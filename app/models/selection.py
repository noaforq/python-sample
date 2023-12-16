from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.choices.scout.selection_route import SelectionRoute
from app.choices.scout.selection_step import SelectionStep
from app.models.base.transaction_base import TransactionBase
from app.models.column_types.int_enum import IntEnum

if TYPE_CHECKING:
    from app.models import Company, Job, ManagedStudent, Message, MessageTempfile, Reaction


class Selection(TransactionBase):
    __tablename__ = "selections"

    company_id: Mapped[int] = mapped_column(sa.ForeignKey("companies.company_id"), comment="企業ID")
    company: Mapped["Company"] = relationship(back_populates="selections")

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    job: Mapped["Job"] = relationship(back_populates="selections")

    reactions: Mapped[list["Reaction"]] = relationship(back_populates="selection")

    student_id: Mapped[int] = mapped_column(sa.ForeignKey("managed_students.student_id", ondelete="CASCADE"), comment="学生の一意の識別子")
    managed_student: Mapped["ManagedStudent"] = relationship(back_populates="selections")
    is_scout_refuse: Mapped[bool] = mapped_column(sa.Boolean(False), comment="")
    route: Mapped[SelectionRoute] = mapped_column(
        IntEnum(SelectionRoute),
        default=SelectionRoute.SCOUT,
        comment="スカウト経由（スカウト非公開求人） or 公開求人経由（スカウト公開求人）",
        index=True,
    )
    step: Mapped[SelectionStep] = mapped_column(
        IntEnum(SelectionStep),
        default=SelectionStep.APPLYING,
        comment="",
        index=True,
    )
    scheduled_start_date: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="")
    scheduled_end_date: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="")
    memo: Mapped[str] = mapped_column(sa.String(255), comment="TechFUL+text型")

    messages: Mapped[list["Message"]] = relationship(back_populates="selection")
    message_tempfiles: Mapped[list["MessageTempfile"]] = relationship(back_populates="selection")
