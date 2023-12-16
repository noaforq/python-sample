import os
from glob import glob
from importlib import import_module
from typing import Any, Callable, Dict, List, Optional, Type, Union

from fastapi.routing import (
    APIRoute,
    APIRouter,
    BaseRoute,
    Default,
    Enum,
    JSONResponse,
    Response,
    Sequence,
    generate_unique_id,
    params,
)

from app.configs import BASE_DIR


def include_routers(
    root_router: APIRouter,
    path: str,
    *,
    prefix: str = "",
    tags: Optional[List[Union[str, Enum]]] = None,
    dependencies: Optional[Sequence[params.Depends]] = None,
    default_response_class: Type[Response] = Default(JSONResponse),
    responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
    callbacks: Optional[List[BaseRoute]] = None,
    deprecated: Optional[bool] = None,
    include_in_schema: bool = True,
    generate_unique_id_function: Callable[[APIRoute], str] = Default(generate_unique_id),
) -> None:
    """path直下のrouterを登録"""
    for r in _get_routers(path):
        root_router.include_router(
            router=r,
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            default_response_class=default_response_class,
            responses=responses,
            callbacks=callbacks,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            generate_unique_id_function=generate_unique_id_function,
        )


def _get_routers(path: str) -> list[APIRouter]:
    """path直下のrouterを取得"""

    routers_path = os.path.join(f"{BASE_DIR}/{path}/[!_]*")
    names = [os.path.splitext(d)[0].replace(BASE_DIR + "/", "").replace("/", ".").replace("\\", ".") for d in glob(routers_path)]

    modules = [import_module(name) for name in names]
    routers = [module.router for module in modules if hasattr(module, "router") and isinstance(module.router, APIRouter)]
    routers.sort(key=lambda m: m.routes[0].path if len(m.routes) == 1 else m.prefix)  # type: ignore
    return routers
