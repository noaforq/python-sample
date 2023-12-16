from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import Company, ManagedStudent

from app.models.base.transaction_base import TransactionBase


class DisclosedStudent(TransactionBase):
    """情報を開示した学生"""

    __tablename__ = "disclosed_students"

    company_id: Mapped[int] = mapped_column(sa.ForeignKey("companies.company_id"), comment="企業ID")
    student_id: Mapped[int] = mapped_column(sa.ForeignKey("managed_students.student_id"), comment="学生ID")

    # relation
    company: Mapped["Company"] = relationship(back_populates="disclosed_students")
    managed_student: Mapped["ManagedStudent"] = relationship(back_populates="disclosed_students")
