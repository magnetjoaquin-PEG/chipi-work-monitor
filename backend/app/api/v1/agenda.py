from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Action
from app.db.models import Risk

router = APIRouter()


@router.get("/today")
def get_today_agenda():

    db = SessionLocal()

    items = []

    risks = db.scalars(
        select(Risk)
    ).all()

    for risk in risks:

        priority = 3

        if risk.severity == "HIGH":
            priority = 1

        elif risk.severity == "MEDIUM":
            priority = 2

        items.append({
            "priority": priority,
            "type": "RISK",
            "title": risk.title,
            "status": risk.status
        })

    actions = db.scalars(
        select(Action)
    ).all()

    for action in actions:

        priority = 3

        if action.priority == "HIGH":
            priority = 1

        elif action.priority == "MEDIUM":
            priority = 2

        items.append({
            "priority": priority,
            "type": "ACTION",
            "title": action.title,
            "status": action.status
        })

    items.sort(
        key=lambda x: x["priority"]
    )

    return {
        "total": len(items),
        "today": items
    }