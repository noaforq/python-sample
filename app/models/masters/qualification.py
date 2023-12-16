import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base.master_base import MasterBase


class MasterQualification(MasterBase):
    """資格"""

    __tablename__ = "m_qualifications"

    value: Mapped[str] = mapped_column(sa.String(63), comment="資格")
