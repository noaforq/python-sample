from fastapi import FastAPI
from fastapi.routing import APIRoute
from humps.main import camelize, pascalize


def update_openapi(app: FastAPI) -> None:
    """
    - operation_idを関数名に設定
    - Formの名前を関数名+Formに設定
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            # operation_idを関数名に設定
            route.operation_id = camelize(route.name)
            # Formの名前を関数名+Formに設定
            if route.body_field and route.body_field.name == "body":
                route.body_field.type_.__name__ = pascalize(route.name) + "Form"
