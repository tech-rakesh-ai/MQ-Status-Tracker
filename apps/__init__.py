from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.tracker.routes import router as tracker_router
from apps.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="v1",
        description=settings.PROJECT_DESCRIPTION,
    )

    origins = [
        "http://localhost",
        "http://localhost:8000"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(tracker_router)

    return app
