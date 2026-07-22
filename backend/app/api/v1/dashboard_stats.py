from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Action, Risk

router = APIRouter()


@router.get("")
def dashboard_stats():

    db = SessionLocal()

    risks = db.scalars(select(Risk)).all()
    actions = db.scalars(select(Action)).all()

    return {
        "risks": {
            "HIGH": len(
                [r for r in risks if r.severity == "HIGH"]
            ),
            "MEDIUM": len(
                [r for r in risks if r.severity == "MEDIUM"]
            ),
            "LOW": len(
                [r for r in risks if r.severity == "LOW"]
            )
        },
        "actions": {
            "OPEN": len(
                [a for a in actions if a.status == "OPEN"]
            ),
            "IN_PROGRESS": len(
                [a for a in actions if a.status == "IN_PROGRESS"]
            ),
            "DONE": len(
                [a for a in actions if a.status == "DONE"]
            )
        }
    }