from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.master_base import MasterBase

if TYPE_CHECKING:
    from app.models import Area


class MasterArea(MasterBase):
    """エリア"""

    __tablename__ = "m_areas"

    value: Mapped[str] = mapped_column(sa.String(63), comment="エリア")

    areas: Mapped[list["Area"]] = relationship(back_populates="m_area")
