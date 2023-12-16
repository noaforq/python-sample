from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase
from app.models.column_types.int_enum import IntEnum

if TYPE_CHECKING:
    from app.models import Job

import app


class RecruitmentStatus(TransactionBase):
    __tablename__ = "recruitment_status"

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    job: Mapped["Job"] = relationship(back_populates="recruitment_statuses")
    recruitment_status: Mapped[app.choices.scout.RecruitmentStatus] = mapped_column(IntEnum(app.choices.scout.RecruitmentStatus), comment="募集採用に関する状況")
    free_input: Mapped[str] = mapped_column(sa.String(1000), comment="TechFUL+text型")
