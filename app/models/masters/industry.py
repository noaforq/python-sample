from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.master_base import MasterBase

if TYPE_CHECKING:
    from app.models.masters.industry_classification import MasterIndustryClassification


class MasterIndustry(MasterBase):
    """業種"""

    __tablename__ = "m_industries"

    industry_classification_id: Mapped[str] = mapped_column(sa.ForeignKey("m_industry_classifications.id", ondelete="CASCADE"), comment="業種分類ID")
    value: Mapped[str] = mapped_column(sa.String(63), comment="業種")

    industry_classification: Mapped["MasterIndustryClassification"] = relationship(back_populates="industries")
