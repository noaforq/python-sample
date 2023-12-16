from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import Selection, Company, ManagedStudent, MessageTempfile

from app.choices.scout import MessageType
from app.models.base.transaction_base import TransactionBase
from app.models.column_types.int_enum import IntEnum


class Message(TransactionBase):
    """メッセージ"""

    __tablename__ = "messages"

    selection_id: Mapped[str] = mapped_column(sa.ForeignKey("selections.id"), comment="選考ID")
    company_id: Mapped[int] = mapped_column(sa.ForeignKey("companies.company_id"), comment="企業ID")
    student_id: Mapped[int] = mapped_column(sa.ForeignKey("managed_students.student_id"), comment="学生ID")
    send_date: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="送信日")
    is_unread: Mapped[bool] = mapped_column(sa.Boolean(False), comment="未読か")
    message_type: Mapped[MessageType] = mapped_column(IntEnum(MessageType), comment="メッセージの種類")
    body: Mapped[str] = mapped_column(sa.Text(), comment="本文")

    # relation
    selection: Mapped["Selection"] = relationship(back_populates="messages")
    company: Mapped["Company"] = relationship(back_populates="messages")
    managed_student: Mapped["ManagedStudent"] = relationship(back_populates="messages")
    message_tempfile: Mapped["MessageTempfile"] = relationship(back_populates="message")
