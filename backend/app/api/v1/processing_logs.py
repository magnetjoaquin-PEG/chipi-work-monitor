from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import ProcessingLog

router = APIRouter()


@router.get("/")
def get_processing_logs():

    db = SessionLocal()

    logs = db.scalars(
        select(ProcessingLog)
    ).all()

    return {
        "total": len(logs),
        "logs": [
            {
                "id": log.id,
                "document_name": log.document_name,
                "actions_created": log.actions_created,
                "risks_created": log.risks_created
            }
            for log in logs
        ]
    }