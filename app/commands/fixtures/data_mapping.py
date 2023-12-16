from app.models.base.common import BaseModel

# fixtureのCSVファイルとFastAPIのModelを紐づける
# ユニットテスト時に自動的にCSVからテスト用のDBにデータが登録される
data_mapping: dict[str, BaseModel] = {
    # "{CSVファイルのパス}": Model
}
