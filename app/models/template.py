from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.choices.scout.template_use_case import TemplateUseCase
from app.models.base.transaction_base import TransactionBase
from app.models.column_types.int_enum import IntEnum

if TYPE_CHECKING:
    from app.models import Company, JobTemplate


class Template(TransactionBase):
    __tablename__ = "templates"

    company_id: Mapped[int] = mapped_column(sa.ForeignKey("companies.company_id", ondelete="CASCADE"), comment="企業の一意の識別子")
    company: Mapped["Company"] = relationship(back_populates="templates")

    use_case: Mapped[TemplateUseCase] = mapped_column(
        IntEnum(TemplateUseCase),
        default=TemplateUseCase.SCOUT_TEMPLATE,
        comment="スカウトテンプレート or メッセージテンプレート",
        index=True,
    )
    no: Mapped[int] = mapped_column(sa.Integer(), comment="")
    name: Mapped[str] = mapped_column(sa.String(100), comment="")
    subject: Mapped[str] = mapped_column(sa.String(100), comment="")
    body: Mapped[str] = mapped_column(sa.TEXT(), comment="TechFUL+text型")

    job_templates: Mapped[list["JobTemplate"]] = relationship(back_populates="template")
