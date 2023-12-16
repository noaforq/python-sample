from fastapi import APIRouter

from app.utils.router import include_routers

router = APIRouter()

include_routers(root_router=router, path="app/routers/v1/selections", prefix="/selections", tags=["selections"])
