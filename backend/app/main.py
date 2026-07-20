from fastapi import FastAPI

from app.api.router import router
from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Chipi Work Monitor",
    version="0.1.0"
)

app.include_router(router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "system": "Chipi Work Monitor",
        "version": "0.1.0"
    }