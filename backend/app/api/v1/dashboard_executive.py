from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import (
    Document,
    Action,
    Risk,
    ProcessingLog
)

router = APIRouter()


@router.get("")
def executive_dashboard():

    db = SessionLocal()

    documents = db.scalars(
        select(Document)
    ).all()

    actions = db.scalars(
        select(Action)
    ).all()

    risks = db.scalars(
        select(Risk)
    ).all()

    logs = db.scalars(
        select(ProcessingLog)
    ).all()

    actions_open = len(
        [a for a in actions if a.status != "DONE"]
    )

    actions_closed = len(
        [a for a in actions if a.status == "DONE"]
    )

    total_actions = len(actions)

    completion_rate = 0

    if total_actions > 0:
        completion_rate = round(
            (actions_closed / total_actions) * 100,
            1
        )

    critical_items = len(
        [
            r
            for r in risks
            if r.severity == "HIGH"
        ]
    )

    top_priority = None

    if risks:
        top_priority = risks[0].title

    elif actions:
        top_priority = actions[0].title

    documents_processed = len(logs)

    actions_generated = sum(
        log.actions_created
        for log in logs
    )

    risks_generated = sum(
        log.risks_created
        for log in logs
    )

    last_document = None

    if logs:
        last_document = logs[-1].document_name

    return {
        "summary": {
            "documents": len(documents),
            "actions_open": actions_open,
            "actions_closed": actions_closed,
            "risks_open": len(risks),
            "documents_processed": documents_processed
        },
        "processing": {
            "actions_generated": actions_generated,
            "risks_generated": risks_generated,
            "last_document": last_document
        },
        "completion_rate": completion_rate,
        "critical_items": critical_items,
        "top_priority": top_priority,
        "system_status": "healthy",
        "project_version": "0.2.0-alpha"
    }