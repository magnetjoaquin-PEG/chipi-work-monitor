from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Action
from app.modules.actions.schemas import ActionCreate

from fastapi import HTTPException
from app.modules.actions.schemas import ActionUpdate

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

@router.patch("/{action_id}")
def update_action(
    action_id: int,
    update: ActionUpdate
):

    db = SessionLocal()

    action = db.get(
        Action,
        action_id
    )

    if not action:
        raise HTTPException(
            status_code=404,
            detail="Action not found"
        )

    action.status = update.status

    db.commit()
    db.refresh(action)

    return {
        "id": action.id,
        "title": action.title,
        "status": action.status
    }