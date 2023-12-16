from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase

if TYPE_CHECKING:
    from app.models.job import Job
    from app.models.masters import MasterFeature


class Feature(TransactionBase):
    __tablename__ = "features"

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    m_feature_id: Mapped[int] = mapped_column(sa.Integer(), comment="特徴マスターの一意の識別子")

    job: Mapped["Job"] = relationship(back_populates="features")
    m_feature: Mapped["MasterFeature"] = relationship(back_populates="features")
