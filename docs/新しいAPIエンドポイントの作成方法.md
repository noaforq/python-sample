# 新しいAPIエンドポイント(Routings; ルーティング)を追加する方法

サーバ起動時に、app/routers配下に存在しているRouterを設定している

```
app/
|___routers/
  |___example/          # APIエンドポイントグループ
    |___  __init__.py   # グループ単位で追加するための基準となるファイル
    |___ get_example.py # APIエンドポイント定義
```

## 既存グループにAPIを追加する時

すでに存在しているAPIエンドポイントグループにAPIを追加するときは、純粋にエンドポイントグループ配下に新しいAPIエンドポイント定義を作成すればよい。
追加すると、`app/routers/__init__.py` でまとめて読み込んでくれる。

## 新規グループを作成し、APIも同時に追加する時

新規のAPIエンドポイントグループを作るときは、`app/routers/{グループ名}/__init__.py`を以下の内容で作り、あとは同じようにAPIエンドポイント定義を作成すればよい。
ファイル名は`{HTTPリクエストメソッド}_{エンドポイントのURIの/を_に置き換え、パスパラメータとクエリパラメータを排したもの}.py`で統一する。この法則で重複した場合に限り、パスパラメータもファイル名に含むことにする。

```python
from fastapi import APIRouter

from app.utils.router import include_routers

router = APIRouter()

include_routers(
    root_router=router,
    path="app/routers/{グループ名}/__init__.py",
    prefix="APIエンドポイントのグループ名",
    tags=["APIエンドポイントのグループ名"],
)
```

# APIエンドポイント作成ことはじめ

[TechFUL+側のサンプル (agree_term.py)](https://github.com/triple-four/scout-api/blob/83a8a25feea064cd5342565c40b9e081f4d3e069/app/routers/common/terms/agree_term.py)

```bash
# 少なくともAPIRouterは必ずimportが必要である
from fastapi import APIRouter, Depends, Path

#------------------- 省略 -------------------#

router = APIRouter()


# エンドポイントURIの定義。最低summaryは書くこと
@router.post("/{term_type}", summary="利用規約同意API(共通)")

# 関数名はPythonで許容されている範囲であれば問題なく動くが、
# スカウト機能ではファイル名に合わせることにする
async def agree_term(
    # 
    user: User = Depends(auth_user),
    session: AsyncSession = Depends(get_session),
    term_type: TermType = Path(..., description=TermType.description()),
) -> None:
    # 最低限関数の説明は書くこと！
    """利用規約同意、再同意
    指定されたTermTypeで最新の利用規約登録
    """
    #------------------- 省略 -------------------#
```

# 動作確認

作成が終わったらPostmanなどのツールを使って自分の作ったAPIエンドポイントのURIへリクエストしてみて動作確認をする。
Docker Desktopでログが見られるので、`500 Internal Server Error` とかその他エラーが出ていないか確認する。

## Git Bash他UNIX互換ターミナルからの確認方法

`curl` で確認することもできる

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"what_is_happiness": "still finding"}' http://127.0.0.1/your-brand-new-api-endpoint
```
