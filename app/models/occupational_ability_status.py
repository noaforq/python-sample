from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase
from app.models.column_types.int_enum import IntEnum

if TYPE_CHECKING:
    from app.models.job import Job

import app


class OccupationalAbilityStatus(TransactionBase):
    __tablename__ = "occupational_ability_status"

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    job: Mapped["Job"] = relationship(back_populates="occupational_ability_statuses")
    occupational_ability_status: Mapped[app.choices.scout.OccupationalAbilityStatus] = mapped_column(IntEnum(app.choices.scout.OccupationalAbilityStatus), comment="職業能力開発・向上に関する状況")
    free_input: Mapped[str] = mapped_column(sa.String(1000), comment="TechFUL+text型")
