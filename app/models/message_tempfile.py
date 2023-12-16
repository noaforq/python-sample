from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import Selection, Message

from app.models.base.transaction_base import TransactionBase


class MessageTempfile(TransactionBase):
    """添付ファイル"""

    __tablename__ = "message_tempfiles"

    selection_id: Mapped[str] = mapped_column(sa.ForeignKey("selections.id"), comment="選考ID")
    message_id: Mapped[str] = mapped_column(sa.ForeignKey("messages.id"), comment="メッセージID")
    file_name: Mapped[str] = mapped_column(sa.String(255), comment="ファイル名")
    path: Mapped[str] = mapped_column(sa.String(255), comment="ファイルパス")

    # relation
    selection: Mapped["Selection"] = relationship(back_populates="message_tempfiles")
    message: Mapped["Message"] = relationship(back_populates="message_tempfile")
