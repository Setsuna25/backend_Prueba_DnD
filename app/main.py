import logging

from fastapi import FastAPI

from app.router import ping as ping_router
from app.router import caracteristica as caracteristica_router
from app.utils.db import create_db_and_tables

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping_router.router, prefix="/ping")
    application.include_router(caracteristica_router.router, prefix="/caracteristica")
    return application


app = create_application()


@app.on_event("startup")
def on_startup():
    log.info("Starting up...")
    create_db_and_tables()


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
