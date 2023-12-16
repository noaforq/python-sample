from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.master_base import MasterBase

if TYPE_CHECKING:
    from app.models import Framework


class MasterFramework(MasterBase):
    """フレームワーク"""

    __tablename__ = "m_frameworks"

    value: Mapped[str] = mapped_column(sa.String(63), comment="フレームワーク")

    frameworks: Mapped[list["Framework"]] = relationship(back_populates="m_framework")
