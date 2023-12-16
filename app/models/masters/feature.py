from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.master_base import MasterBase

if TYPE_CHECKING:
    from app.models import Feature


class MasterFeature(MasterBase):
    """特徴"""

    __tablename__ = "m_features"

    value: Mapped[str] = mapped_column(sa.String(63), comment="特徴")

    features: Mapped[list["Feature"]] = relationship(back_populates="m_feature")
