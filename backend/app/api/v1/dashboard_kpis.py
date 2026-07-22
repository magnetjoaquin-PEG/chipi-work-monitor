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
def dashboard_kpis():

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

    return {
        "cards": [
            {
                "title": "Open Risks",
                "value": len(risks),
                "color": "red"
            },
            {
                "title": "Open Actions",
                "value": len(
                    [
                        a
                        for a in actions
                        if a.status != "DONE"
                    ]
                ),
                "color": "orange"
            },
            {
                "title": "Documents Processed",
                "value": len(logs),
                "color": "blue"
            },
            {
                "title": "Actions Generated",
                "value": sum(
                    log.actions_created
                    for log in logs
                ),
                "color": "green"
            }
        ]
    }