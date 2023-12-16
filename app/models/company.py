from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import DisclosedStudent, Job, FavoriteJob, Template, Reaction, Selection, Message

from app.models.base.transaction_base import TransactionBase


class Company(TransactionBase):
    """企業"""

    __tablename__ = "companies"

    company_id: Mapped[int] = mapped_column(sa.Integer(), unique=True, comment="企業ID")
    name: Mapped[str] = mapped_column(sa.String(63), comment="名称")
    max_scouts: Mapped[int] = mapped_column(sa.Integer(), comment="契約スカウト数")
    contract_expiration_date: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), comment="契約満了日")

    # relation
    disclosed_students: Mapped[list["DisclosedStudent"]] = relationship(back_populates="company")
    jobs: Mapped[list["Job"]] = relationship(back_populates="company")
    favorite_jobs: Mapped[list["FavoriteJob"]] = relationship(back_populates="company")
    templates: Mapped[list["Template"]] = relationship(back_populates="company")
    reactions: Mapped[list["Reaction"]] = relationship(back_populates="company")
    selections: Mapped[list["Selection"]] = relationship(back_populates="company")
    messages: Mapped[list["Message"]] = relationship(back_populates="company")
