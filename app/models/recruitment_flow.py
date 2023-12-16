from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase

if TYPE_CHECKING:
    from app.models.job import Job


class RecruitmentFlow(TransactionBase):
    __tablename__ = "recruitment_flows"

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="企業の一意の識別子")
    job: Mapped["Job"] = relationship(back_populates="recruitment_flows")

    free_input: Mapped[str] = mapped_column(sa.String(1000), comment="TechFUL+text型")
