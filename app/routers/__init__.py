from fastapi import APIRouter

from app.utils.router import include_routers

# TODO: 一度にあるディレクトリ配下のRouterを登録してしまうと、ホットリロードの度に時間がかかってしまうので
# 対策をしたい
router = APIRouter()

include_routers(router, "app/routers")
