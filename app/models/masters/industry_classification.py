from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.master_base import MasterBase

if TYPE_CHECKING:
    from app.models.masters.industry import MasterIndustry


class MasterIndustryClassification(MasterBase):
    """業種分類"""

    __tablename__ = "m_industry_classifications"

    value: Mapped[str] = mapped_column(sa.String(63), comment="業種分類")

    industries: Mapped[list["MasterIndustry"]] = relationship(back_populates="industry_classification")
