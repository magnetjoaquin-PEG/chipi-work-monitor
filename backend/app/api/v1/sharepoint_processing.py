from fastapi import APIRouter
from pydantic import BaseModel

from app.db.database import SessionLocal
from app.db.models import ProcessingLog

router = APIRouter()


class ProcessDocumentRequest(BaseModel):
    name: str


@router.post("/process-document")
def process_document(
    request: ProcessDocumentRequest
):

    db = SessionLocal()

    log = ProcessingLog(
        document_name=request.name,
        actions_created=1,
        risks_created=1
    )

    db.add(log)
    db.commit()

    return {
        "document": request.name,
        "status": "processed",
        "actions_created": 1,
        "risks_created": 1
    }