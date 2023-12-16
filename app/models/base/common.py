from typing import Any, Sequence, Type, TypeVar

import sqlalchemy as sa
from sqlalchemy import MetaData, Select, delete, func, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql._typing import _ColumnExpressionOrStrLabelArgument

from app.choices.params.locale import Locale

MODEL = TypeVar("MODEL", bound="BaseModel")


class BaseModel(DeclarativeBase):
    __abstract__ = True
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    _locale: Locale | None = None

    def set_locale(self: MODEL, locale: Locale) -> MODEL:
        if not isinstance(locale, Locale):
            raise LocaleError

        self._locale = locale
        return self

    @classmethod
    def set_locale_list(cls: Type[MODEL], models: list[MODEL], locale: Locale) -> list[MODEL]:
        if not isinstance(locale, Locale):
            raise LocaleError

        return [model.set_locale(locale) for model in models]

    @classmethod
    async def get(
        cls: Type[MODEL],
        session: AsyncSession,
        *args: Any,
        options: list[sa.sql.base.ExecutableOption] | None = None,
        **kwargs: Any,
    ) -> MODEL:
        """
        Args:
            session:
            options: options
            *args: whereパラメータ
            **kwargs: filter_byパラメータ

        Returns:
            model
        """
        stmt = select(cls).distinct()
        if args:
            stmt = stmt.where(*args)
        if kwargs:
            stmt = stmt.filter_by(**kwargs)
        if options:
            stmt = stmt.options(*options)
        result = await session.execute(stmt)
        return result.scalar_one()

    @classmethod
    async def get_all(
        cls: Type[MODEL],
        session: AsyncSession,
        *args: Any,
        options: list[sa.sql.base.ExecutableOption] | None = None,
        order_by: _ColumnExpressionOrStrLabelArgument[Any] | None = None,
        **kwargs: Any,
    ) -> Sequence[MODEL]:
        """
        Return all model list
        Args:
            session:
            options: options
            order_by: order_byパラメータ
            *args: whereパラメータ
            **kwargs: filter_byパラメータ

        Returns:
            list[model]
        """
        stmt = select(cls).distinct()
        if args:
            stmt = stmt.where(*args)
        if kwargs:
            stmt = stmt.filter_by(**kwargs)
        if options:
            stmt = stmt.options(*options)
        if order_by is not None:
            stmt = stmt.order_by(order_by)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def get_or_none(
        cls: Type[MODEL],
        session: AsyncSession,
        *args: Any,
        options: list[sa.sql.base.ExecutableOption] | None = None,
        **kwargs: Any,
    ) -> MODEL | None:
        """
        Args:
            session:
            options: options
            *args: whereパラメータ
            **kwargs: filter_byパラメータ

        Returns:
            model
        """
        stmt = select(cls).distinct()
        if args:
            stmt = stmt.where(*args)
        if kwargs:
            stmt = stmt.filter_by(**kwargs)
        if options:
            stmt = stmt.options(*options)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def create(cls: Type[MODEL], session: AsyncSession, **kwargs: Any) -> MODEL:
        """
        Args:
            session:
            **kwargs: 作成時に使用するパラメータ

        Returns:
            model
        """
        stmt = insert(cls).values(**kwargs).returning(cls)
        result = await session.execute(stmt)
        return result.scalar_one()

    @classmethod
    async def bulk_create(cls: Type[MODEL], session: AsyncSession, values: list[dict]) -> Sequence[MODEL]:
        """
        Args:
            session:
            values: 作成データのリスト

        Returns:
            model
        """
        if not values:
            return []

        return (await session.execute(insert(cls).returning(cls), values)).scalars().all()

    async def update(self: MODEL, session: AsyncSession, **kwargs: Any) -> MODEL:
        """
        Args:
            session:
            **kwargs: 更新パラメータ

        Returns:
            (model, is_created)
        """
        model_class = type(self)
        stmt = update(model_class).where(model_class.id == self.id).values(**kwargs).returning(model_class)  # type: ignore
        result = await session.execute(stmt)
        return result.scalar_one()

    async def delete(self, session: AsyncSession) -> None:
        model_type = type(self)
        stmt = delete(model_type).where(model_type.id == self.id)  # type: ignore
        await session.execute(stmt)

    @classmethod
    async def get_or_create(cls: Type[MODEL], session: AsyncSession, defaults: dict | None = None, **kwargs: Any) -> tuple[MODEL, bool]:
        """
        Args:
            session:
            defaults: 作成時に使用するパラメータ
            **kwargs: 取得、作成時に使用するパラメータ

        Returns:
            (model, created)
        """
        if defaults is None:
            defaults = {}

        stmt = select(cls).filter_by(**kwargs)
        result = await session.execute(stmt)
        model = result.scalar_one_or_none()

        if model:  # get
            return model, False
        else:  # create
            if "id" in kwargs.keys():
                kwargs.pop("id")
            stmt = insert(cls).values(**defaults, **kwargs).returning(cls)  # type: ignore
            result = await session.execute(stmt)
            return result.scalar_one(), True

    @classmethod
    async def update_or_create(cls: Type[MODEL], session: AsyncSession, defaults: dict | None = None, **kwargs: Any) -> tuple[MODEL, bool]:
        """
        Args:
            session:
            defaults: 作成時に使用するパラメータ
            **kwargs: 取得、作成時に使用するパラメータ

        Returns:
            (model, created)
        """
        if defaults is None:
            defaults = {}

        stmt = select(cls).filter_by(**kwargs)

        print("Hogefuga")
        print(cls)

        result = await session.execute(stmt)
        model = result.scalar_one_or_none()

        if model:  # update
            stmt = update(cls).filter_by(**kwargs).values(**defaults).returning(cls)  # type: ignore
            result = await session.execute(stmt)
            return result.scalar_one(), False
        else:  # create
            if "id" in kwargs.keys():
                kwargs.pop("id")
            stmt = insert(cls).values(**defaults, **kwargs).returning(cls)  # type: ignore
            result = await session.execute(stmt)
            return result.scalar_one(), True

    @classmethod
    async def count(cls, session: AsyncSession, stmt: Select) -> int:
        return (await session.execute(select(func.count()).select_from(stmt.subquery()))).scalar_one()

    @classmethod
    def json_list(cls, models: Sequence[MODEL], *args: str, **kwargs: str) -> list[dict]:
        """modelのリストからdictに変換(リレーション先は自動取得)
        Args:
            models: モデルのリスト
            *args: プロパティなどの名前
            **kwargs: {変換後の名前: プロパティなどの名前}

        Examples:
            User.json_list(users, "full_name")
            User.json_list(users, organization_name="organization__organization_name")
        """
        fetch_fields = list(args) + list(kwargs.values())
        return [cls._create_new_fields(cls._convert(model, fetch_fields), kwargs) for model in models]

    def json(self, *args: str, **kwargs: str) -> dict:
        """modelからdictに変換(リレーション先は自動取得)
        Args:
            *args: プロパティなどの名前
            **kwargs: {変換後の名前: プロパティなどの名前}

        Examples:
            user.json("full_name")
            user.json(organization_name="organization__organization_name")
        """
        fetch_fields = list(args) + list(kwargs.values())
        return self._create_new_fields(self._convert(self, fetch_fields), kwargs)

    @classmethod
    def _create_new_fields(cls, dict_fields: dict, new_field_dict: dict) -> dict:
        for k, v in new_field_dict.items():
            attrs = v.split(".")
            value: Any = dict_fields
            for attr in attrs:
                if isinstance(value, list):
                    value = [v.get(attr) if isinstance(v, dict) else value for v in value]
                    continue

                value = value.get(attr) if isinstance(value, dict) else value

            dict_fields[k] = value
        return dict_fields

    @classmethod
    def _convert(cls, model: MODEL, fetch_fields: list[str], depth: int = 0) -> dict:
        # 現在のdepthに対応するfetch_field一覧を取得
        new_fetch_fields = tuple(field for field in fetch_fields if len(field.split(".")) >= depth + 1)
        current_fetch_fields = set(field.split(".")[depth] for field in new_fetch_fields)

        # 通常のフィールドを取得
        dict_model: dict = {k: v for k, v in vars(model).items() if not k.startswith("_")}

        # リレーションのフィールドを取得
        for field in current_fetch_fields:
            value = getattr(model, field)
            is_property = isinstance(getattr(model.__class__, field), property)
            next_fetch_fields = [f for f in new_fetch_fields if f.split(".")[depth] == field]

            if (field in dict_model.keys() or is_property) and isinstance(value, list) and all(isinstance(v, BaseModel) for v in value):
                dict_model[field] = [cls._convert(v, next_fetch_fields, depth + 1) for v in value]
            elif (field in dict_model.keys() or is_property) and isinstance(value, BaseModel):
                dict_model[field] = cls._convert(value, next_fetch_fields, depth + 1)
            else:
                dict_model[field] = value

        return dict_model


class LocaleError(Exception):
    """ロケールが正しく設定されていない場合に投げる例外"""
