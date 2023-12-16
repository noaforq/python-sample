from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase
from app.models.column_types.int_enum import IntEnum

if TYPE_CHECKING:
    from app.models import Job

import app


class EmploymentManagementStatus(TransactionBase):
    __tablename__ = "employment_management_status"

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    job: Mapped["Job"] = relationship(back_populates="employment_management_statuses")
    employment_management_status: Mapped[app.choices.scout.EmploymentManagementStatus] = mapped_column(IntEnum(app.choices.scout.EmploymentManagementStatus), comment="企業における雇用管理に関する状況")
    free_input: Mapped[str] = mapped_column(sa.String(1000), comment="TechFUL+text型")
