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
def workspace():

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

    high_risks = [
        r
        for r in risks
        if r.severity == "HIGH"
    ]

    return {
        "home": {
            "greeting": "Bienvenido a Chipi",
            "top_priority": (
                high_risks[0].title
                if high_risks
                else None
            )
        },
        "kpis": {
            "open_risks": len(risks),
            "open_actions": len(open_actions),
            "documents_processed": len(logs)
        },
        "risk_board": {
            "high": [
                {
                    "id": r.id,
                    "title": r.title
                }
                for r in high_risks
            ]
        },
        "action_board": {
            "open": [
                {
                    "id": a.id,
                    "title": a.title
                }
                for a in open_actions
            ]
        },
        "processing_center": [
            {
                "id": log.id,
                "document": log.document_name,
                "status": "SUCCESS"
            }
            for log in sorted(
                logs,
                key=lambda x: x.id,
                reverse=True
            )[:5]
        ]
    }