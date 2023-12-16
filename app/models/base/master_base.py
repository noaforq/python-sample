import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base.common import BaseModel


class MasterBase(BaseModel):

    __abstract__ = True

    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True, comment="ID")
    order: Mapped[int] = mapped_column(sa.Integer(), comment="表示順")
