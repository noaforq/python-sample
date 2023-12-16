from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.master_base import MasterBase

if TYPE_CHECKING:
    from app.models import Skill


class MasterSkill(MasterBase):
    """スキル"""

    __tablename__ = "m_skills"

    value: Mapped[str] = mapped_column(sa.String(63), comment="スキル")

    skills: Mapped[list["Skill"]] = relationship(back_populates="m_skill")
