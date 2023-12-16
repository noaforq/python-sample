import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base.master_base import MasterBase


class MasterProgrammingExperience(MasterBase):
    """プログラミング経験"""

    __tablename__ = "m_programming_experiences"

    value: Mapped[str] = mapped_column(sa.String(63), comment="プログラミング経験")
