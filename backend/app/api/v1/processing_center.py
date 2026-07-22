from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import ProcessingLog

router = APIRouter()


@router.get("")
def processing_center():

    db = SessionLocal()

    logs = db.scalars(
        select(ProcessingLog)
    ).all()

    logs = sorted(
        logs,
        key=lambda x: x.id,
        reverse=True
    )

    return {
        "recent_documents": [
            {
                "id": log.id,
                "document": log.document_name,
                "status": "SUCCESS",
                "actions_created": log.actions_created,
                "risks_created": log.risks_created
            }
            for log in logs
        ]
    }