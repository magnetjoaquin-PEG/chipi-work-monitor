from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Document
from app.db.models import Action
from app.db.models import Risk

router = APIRouter()


@router.get("")
def executive_dashboard():

    db = SessionLocal()

    documents = db.scalars(select(Document)).all()
    actions = db.scalars(select(Action)).all()
    risks = db.scalars(select(Risk)).all()

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

    return {
        "summary": {
            "documents": len(documents),
            "actions_open": actions_open,
            "actions_closed": actions_closed,
            "risks_open": len(risks)
        },
        "completion_rate": completion_rate,
        "critical_items": critical_items,
        "top_priority": top_priority,
        "system_status": "healthy",
        "project_version": "0.1.6-alpha"
    }