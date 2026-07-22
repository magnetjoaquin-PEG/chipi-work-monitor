from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Action

router = APIRouter()


@router.get("")
def action_board():

    db = SessionLocal()

    actions = db.scalars(
        select(Action)
    ).all()

    return {
        "open": [
            {
                "id": a.id,
                "title": a.title
            }
            for a in actions
            if a.status == "OPEN"
        ],
        "in_progress": [
            {
                "id": a.id,
                "title": a.title
            }
            for a in actions
            if a.status == "IN_PROGRESS"
        ],
        "done": [
            {
                "id": a.id,
                "title": a.title
            }
            for a in actions
            if a.status == "DONE"
        ]
    }