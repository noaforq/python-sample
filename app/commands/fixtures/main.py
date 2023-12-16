import csv

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.commands import run
from app.commands.fixtures.data_mapping import data_mapping
from app.commands.fixtures.type_mapping import get_type_mapping
from app.configs import BASE_DIR


async def register_fixtures(session: AsyncSession) -> None:
    await register_fixtures_with_mapping(session, data_mapping)


async def register_fixtures_with_mapping(session: AsyncSession, mapping: dict) -> None:
    for filename, model_class in mapping.items():
        with open(f"{BASE_DIR}/app/commands/fixtures/csv/{filename}") as f:
            reader = csv.reader(f)

            # ヘッダー取得
            headers = reader.__next__()

            # 型変換用の関数を取得
            conv_funcs = []
            for header in headers:
                python_type = getattr(model_class, header).type.python_type
                conv_func = get_type_mapping()[python_type]
                conv_funcs.append(conv_func)

            # データ登録
            for row in reader:
                row_dict = {headers[i]: conv_funcs[i](row[i]) for i in range(len(headers))}
                id_ = row_dict.pop("id")
                _, created = await model_class.update_or_create(session, id=id_, defaults=row_dict)

            # テーブルのシーケンス更新
            current_sequence = (await session.execute(select(func.max(model_class.id)))).scalar()
            stmt_update_sequesnce = f"SELECT setval('{model_class.__tablename__}_id_seq', {current_sequence});"
            await session.execute(text(stmt_update_sequesnce))


if __name__ == "__main__":
    run(register_fixtures)
