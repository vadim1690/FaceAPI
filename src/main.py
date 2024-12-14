import uvicorn
from fastapi import FastAPI
from src.core.config import settings
from src.core.logging_config import logger
from src.api.v1.routes import router as v1_router

def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.APP_NAME,
        description="An API that detects faces, crops them, and generates embeddings.",
        version="1.0.0"
    )

    application.include_router(v1_router, prefix="/api/v1", tags=["Face Operations"])
    return application

app = create_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
