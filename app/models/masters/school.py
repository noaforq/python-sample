import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base.master_base import MasterBase


class MasterSchool(MasterBase):
    """学校"""

    __tablename__ = "m_schools"

    value: Mapped[str] = mapped_column(sa.String(63), comment="学校")
