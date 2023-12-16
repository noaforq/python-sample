from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase

if TYPE_CHECKING:
    from app.models import Job


class CommutingTime(TransactionBase):
    __tablename__ = "commuting_times"

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    job: Mapped["Job"] = relationship(back_populates="commuting_times")

    commuting_time_from: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="")
    commuting_time_to: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="")
