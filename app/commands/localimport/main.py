import glob
import os

import pandas
from sqlalchemy import create_engine, text

if __name__ == "__main__":
    # app/commands/fixture/csv配下にあるCSVファイルからローカルのDBにレコードをぶち込む
    # CSVファイルの名前はテーブル名と一致していなければならない
    engine = create_engine("postgresql://postgres:postgres@scout-db:1836/main")

    with engine.connect() as connection:
        source_csv_files = glob.glob("app/commands/fixtures/csv/*.csv")
        csv_file_count = source_csv_files.__len__()

        print("Total number of CSV files: {}".format(csv_file_count))

        process_done_count = 0
        for source_csv_file in source_csv_files:
            print(
                "Importing {} ({}% done, {} of {})".format(
                    source_csv_file,
                    int(process_done_count / csv_file_count * 100),
                    process_done_count + 1,
                    csv_file_count,
                )
            )

            pandas_csv = pandas.read_csv(source_csv_file)
            table_name = os.path.basename(source_csv_file).replace(".csv", "")

            # 一旦外部キーを無効にしないと投入できないため無効化する
            connection.execute(text("ALTER TABLE " + table_name + " DISABLE TRIGGER ALL;"))
            pandas_csv.to_sql(table_name, con=connection, if_exists="append", index=False)
            connection.execute(text("ALTER TABLE " + table_name + " ENABLE TRIGGER ALL;"))

            # connection.executeがどうやらTRANSACTIONを開始するらしく、これをしないと投入結果が反映されない
            connection.execute(text("COMMIT;"))

            print("Importing {} into a table {} has been completed, continuing next".format(source_csv_file, table_name))
            process_done_count += 1

        print("Import done.")
