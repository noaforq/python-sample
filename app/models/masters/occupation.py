import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base.master_base import MasterBase


class MasterOccupation(MasterBase):
    """職種"""

    __tablename__ = "m_occupations"

    value: Mapped[str] = mapped_column(sa.String(63), comment="職種")
