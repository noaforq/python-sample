from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase

if TYPE_CHECKING:
    from app.models import Job
    from app.models.masters import MasterArea


class Area(TransactionBase):
    __tablename__ = "areas"

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    m_area_id: Mapped[int] = mapped_column(sa.Integer(), comment="エリアマスターの一意の識別子")

    job: Mapped["Job"] = relationship(back_populates="areas")
    m_area: Mapped["MasterArea"] = relationship(back_populates="areas")
