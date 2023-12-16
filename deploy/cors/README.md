# CloudStorageバケットにCORSを適用するためのREADME

### CORSの設定方法
- Googleログイン
``` shell
gcloud auth login
```

- GCPプロジェクトを切り替える
``` shell
gcloud config set project プロジェクトID
```

- CORSを適用する
``` shell
cd ./deploy/cors
gcloud storage buckets update CloudStorageのURL --cors-file=CORSファイル名

# 実行例)
# gcloud storage buckets update gs://techful-private --cors-file=cors_techful_private_stg.json
# ⠼Updating gs://techful-private/...
#  Completed 1
```

### GCPプロジェクト
| 環境 | プロジェクトID |
| --- | --- |
| ステージング | techful-plus-staging |
| 本番 | techful-plus |

### CloudStorageのURL
| 環境 | URL |
| --- | --- |
| ステージング | gs://techful-private |
| 本番 | gs://techful-plus-private |

### CORSファイル
| 環境 | CORSファイル名 |
| --- | --- |
| ステージング | cors_techful_private_stg.json |
| 本番 | cors_techful_private_prod.json |
