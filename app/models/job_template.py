from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base.transaction_base import TransactionBase

if TYPE_CHECKING:
    from app.models import Job, Template


class JobTemplate(TransactionBase):
    __tablename__ = "job_templates"

    job_id: Mapped[int] = mapped_column(sa.ForeignKey("jobs.id", ondelete="CASCADE"), comment="求人ID")
    job: Mapped["Job"] = relationship(back_populates="job_templates")

    template_id: Mapped[int] = mapped_column(sa.ForeignKey("templates.id", ondelete="CASCADE"), comment="テンプレートID")
    template: Mapped["Template"] = relationship(back_populates="job_templates")
