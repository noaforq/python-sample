from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models import Job
    from app.models.masters import MasterSkill

from app.models.base.transaction_base import TransactionBase


class Skill(TransactionBase):
    """求人：スキル"""

    __tablename__ = "skills"

    job_id: Mapped[str] = mapped_column(sa.ForeignKey("jobs.id"), comment="求人ID")
    m_skill_id: Mapped[int] = mapped_column(sa.Integer(), comment="スキルID")

    # relation
    job: Mapped["Job"] = relationship(back_populates="skills")
    m_skill: Mapped["MasterSkill"] = relationship(back_populates="skills")
