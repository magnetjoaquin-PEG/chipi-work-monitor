from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Action
from app.modules.actions.schemas import ActionCreate

router = APIRouter()


@router.get("")
def get_actions():

    db = SessionLocal()

    actions = db.scalars(
        select(Action)
    ).all()

    return {
        "total": len(actions),
        "actions": [
            {
                "id": a.id,
                "title": a.title,
                "description": a.description,
                "priority": a.priority,
                "status": a.status
            }
            for a in actions
        ]
    }


@router.post("")
def create_action(action: ActionCreate):

    db = SessionLocal()

    new_action = Action(
        title=action.title,
        description=action.description,
        priority=action.priority,
        status="OPEN"
    )

    db.add(new_action)
    db.commit()
    db.refresh(new_action)

    return {
        "id": new_action.id,
        "status": "created"
    }