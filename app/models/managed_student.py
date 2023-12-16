from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import DisclosedStudent, FavoriteJob, Reaction, Selection, Message

from app.models.base.transaction_base import TransactionBase


class ManagedStudent(TransactionBase):
    """管理対象の学生"""

    __tablename__ = "managed_students"

    student_id: Mapped[int] = mapped_column(sa.Integer(), unique=True, comment="学生ID")
    account_name: Mapped[str] = mapped_column(sa.String(150), comment="アカウント名")
    display_name: Mapped[str] = mapped_column(sa.String(200), comment="表示名")

    # relation
    disclosed_students: Mapped[list["DisclosedStudent"]] = relationship(back_populates="managed_student")
    favorite_jobs: Mapped[list["FavoriteJob"]] = relationship(back_populates="managed_student")
    reactions: Mapped[list["Reaction"]] = relationship(back_populates="managed_student")
    selections: Mapped[list["Selection"]] = relationship(back_populates="managed_student")
    messages: Mapped[list["Message"]] = relationship(back_populates="managed_student")
