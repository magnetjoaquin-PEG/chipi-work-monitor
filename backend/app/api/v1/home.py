from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import (
    Action,
    Risk,
    ProcessingLog
)

router = APIRouter()


@router.get("")
def home():

    db = SessionLocal()

    actions = db.scalars(
        select(Action)
    ).all()

    risks = db.scalars(
        select(Risk)
    ).all()

    logs = db.scalars(
        select(ProcessingLog)
    ).all()

    open_actions = [
        a
        for a in actions
        if a.status != "DONE"
    ]

    high_priority_risks = [
        r
        for r in risks
        if r.severity == "HIGH"
    ]

    recent_processing = [
        {
            "document": log.document_name,
            "status": "SUCCESS"
        }
        for log in sorted(
            logs,
            key=lambda x: x.id,
            reverse=True
        )[:5]
    ]

    top_priority = None

    if high_priority_risks:
        top_priority = high_priority_risks[0].title

    elif open_actions:
        top_priority = open_actions[0].title

    return {
        "greeting": "Bienvenido a Chipi",
        "kpis": {
            "open_risks": len(risks),
            "open_actions": len(open_actions),
            "documents_processed": len(logs)
        },
        "recent_processing": recent_processing,
        "high_priority_risks": [
            {
                "id": r.id,
                "title": r.title
            }
            for r in high_priority_risks[:5]
        ],
        "pending_actions": [
            {
                "id": a.id,
                "title": a.title
            }
            for a in open_actions[:5]
        ],
        "top_priority": top_priority
    }