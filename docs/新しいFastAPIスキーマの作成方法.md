# 新しいFastAPIスキーマ (FastAPI Schemas) の作成方法

APIエンドポイントで受け取る・レスポンスとして返す（Request/Response）データの型を厳密に定義し、APIエンドポイントに設定する。

## 流れ

1. FastAPIスキーマを定義する
2. APIエンドポイントに設定する
3. 動作確認する

## 詳細説明

### 1. FastAPIスキーマを定義する

```
app/
|___schemas/
  |___example/         # FastAPIスキーマグループ
    |___  __init__.py  # グループ単位で追加するための基準となるファイル
    |___ example_in.py # FastAPIスキーマ定義
```

#### 例

`get_example.py` というファイル名で定義しているAPIエンドポイントのリクエスト・レスポンスを定義したい場合は、

```python:example_request.py
from datetime import datetime

from pydantic import Field

from app.schemas.base import PydanticModel



# リクエストボディに含めるパラメータを定義していく
class ExampleRequest(PydanticModel):
  example: int = Field(..., description="サンプル")
  """
  description: 説明

  ちなみに、以下のような制約を追加することもできる。

  * gt = greater than (nより大きい)
  * ge = greater or equals (n以上)
  * lt = less than (nより小さい)
  * le = less or equals (n以下)
  * regex = regular expression (正規表現)
  """
```

```python:example_response.py
class ExampleResponse(PydanticModel):
  example: int = Field(..., description="サンプル")
```

### 2. APIエンドポイントに設定する

```python
@router.get(
  "/example/{path_parameter}",             # パスパラメータはここに記載する
  response_model=ExampleResponse,          # 1.で定義したレスポンス用FastAPIスキーマを指定する
  status_code=status.HTTP_200_OK,          # 成功時のHTTPステータスコードを指定する
  responses=error_response(NotFound)       # エラー時のエラーを指定する (app/exceptions.pyを参考)
)
async def get_example(
  example_request: ExampleRequest,         # 1.で定義したリクエスト用FastAPIスキーマを指定
  session: AsyncSession = Depends(session) # 下記参照
  """
  AsyncSession

  https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#sqlalchemy.ext.asyncio.AsyncSession
  "The AsyncSession object is a mutable, stateful object which represents a single, stateful database transaction in progress."
  → 単一の状態を持った、進行中のデータベーストランザクションを表す
  """
)
```

### 3. 動作確認する

#### 動作確認

作成が終わったらPostmanなどのツールを使って自分の作ったAPIエンドポイントのURIへリクエストしてみて動作確認をする。
Docker Desktopでログが見られるので、`500 Internal Server Error` とかその他エラーが出ていないか確認する。

#### Git Bash他UNIX互換ターミナルからの確認方法

`curl` で確認することもできる

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"what_is_happiness": "still finding"}' http://127.0.0.1/your-brand-new-api-endpoint
```

