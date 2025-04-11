from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from bt_users.core.models import db_helper
from core.config import settings
from api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(
    api_router,
    prefix=settings.api.prefix
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.server_host,
        port=settings.run.server_port, 
        reload = True
    )