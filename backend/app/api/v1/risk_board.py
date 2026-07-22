from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Risk

router = APIRouter()


@router.get("")
def risk_board():

    db = SessionLocal()

    risks = db.scalars(
        select(Risk)
    ).all()

    return {
        "high": [
            {
                "id": r.id,
                "title": r.title
            }
            for r in risks
            if r.severity == "HIGH"
        ],
        "medium": [
            {
                "id": r.id,
                "title": r.title
            }
            for r in risks
            if r.severity == "MEDIUM"
        ],
        "low": [
            {
                "id": r.id,
                "title": r.title
            }
            for r in risks
            if r.severity == "LOW"
        ]
    }