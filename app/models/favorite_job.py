from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import ManagedStudent, Company, Job

from app.models.base.transaction_base import TransactionBase


class FavoriteJob(TransactionBase):
    """学生のお気に入り求人"""

    __tablename__ = "favorite_jobs"

    student_id: Mapped[int] = mapped_column(sa.ForeignKey("managed_students.student_id"), comment="学生ID")
    company_id: Mapped[int] = mapped_column(sa.ForeignKey("companies.company_id"), comment="企業ID")
    job_id: Mapped[str] = mapped_column(sa.ForeignKey("jobs.id"), comment="求人ID")

    # relation
    managed_student: Mapped["ManagedStudent"] = relationship(back_populates="favorite_jobs")
    company: Mapped["Company"] = relationship(back_populates="favorite_jobs")
    job: Mapped["Job"] = relationship(back_populates="favorite_jobs")
