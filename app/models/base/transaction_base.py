import uuid
from datetime import datetime, timezone

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.models.base.common import BaseModel


class TransactionBase(BaseModel):

    __abstract__ = True

    id: Mapped[str] = mapped_column(
        sa.String(36),
        primary_key=True,
        comment="ID",
        # server_default=str(uuid.uuid4()),
        default=lambda: str(uuid.uuid4()),
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        server_default=func.now(),
        default=lambda: datetime.now(timezone.utc),
        comment="作成日時",
    )
    created_user_id: Mapped[int] = mapped_column(sa.Integer(), comment="作成ユーザーID")
    updated_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        server_default=func.now(),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        comment="更新日時",
    )
    updated_user_id: Mapped[int] = mapped_column(sa.Integer(), comment="作成ユーザーID")
    disabled_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), nullable=True, comment="削除日時")
    disabled_user_id: Mapped[int] = mapped_column(sa.Integer(), nullable=True, comment="作成ユーザーID")
    is_disabled: Mapped[bool] = mapped_column(sa.Boolean(), default=False, index=True, comment="削除フラグ")
