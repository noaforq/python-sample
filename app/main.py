from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.configs import BASE_DIR, STATIC_DIR, STATIC_URL, settings
from app.exceptions.exception_handlers import add_exception_handlers
from app.exceptions.schemas import ValidationError
from app.middlewares import add_middlewares
from app.routers import router
from app.utils.openapi import update_openapi

app = FastAPI(
    title="TechFUL API",
    docs_url="/docs" if settings.show_openapi_docs else None,
    redoc_url="/redoc" if settings.show_openapi_docs else None,
    openapi_url="/openapi.json" if settings.show_openapi_docs else None,
    swagger_ui_parameters={
        "displayRequestDuration": True,
        "displayOperationId": True,
        "operationsSorter": "alpha",
        "tagsSorter": "alpha",
        "filter": True,
    },
    servers=[
        {"url": settings.server_url, "description": "api"},
        {"url": settings.mock_server_url, "description": "mock"},
    ],
)

# ローカルストレージ設定
if not settings.use_cloud_storage:
    app.mount(f"/{STATIC_URL}", StaticFiles(directory=f"{BASE_DIR}/{STATIC_DIR}"), name="static")


# router設定
app.include_router(router, responses={422: {"model": ValidationError, "description": "バリデーションエラー"}})

# middleware設定
add_middlewares(app)

# exception_handler設定
add_exception_handlers(app)

# openapiの設定
update_openapi(app)

# プロファイラー設定
if settings.enabled_profiler:
    import googlecloudprofiler

    # Profiler initialization. It starts a daemon thread which continuously
    # collects and uploads profiles. Best done as early as possible.
    try:
        # service and service_version can be automatically inferred when
        # running on App Engine. project_id must be set if not running
        # on GCP.
        googlecloudprofiler.start(verbose=settings.profiler_verbose)
    except (ValueError, NotImplementedError) as exc:
        print(exc)  # Handle errors here
