from fastapi import FastAPI
import uvicorn

from api import router as api_router


main_app = FastAPI()
main_app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app", 
        reload = True
    )