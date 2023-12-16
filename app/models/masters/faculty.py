import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base.master_base import MasterBase


class MasterFaculty(MasterBase):
    """学部"""

    __tablename__ = "m_faculties"

    value: Mapped[str] = mapped_column(sa.String(63), comment="学部")
