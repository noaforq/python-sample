from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import Job
    from app.models.masters import MasterFramework

from app.models.base.transaction_base import TransactionBase


class Framework(TransactionBase):
    """求人：フレームワーク"""

    __tablename__ = "frameworks"

    job_id: Mapped[str] = mapped_column(sa.ForeignKey("jobs.id"), comment="求人ID")
    m_framework_id: Mapped[int] = mapped_column(sa.Integer(), comment="フレームワークID")

    # relation
    job: Mapped["Job"] = relationship(back_populates="frameworks")
    m_framework: Mapped["MasterFramework"] = relationship(back_populates="frameworks")
