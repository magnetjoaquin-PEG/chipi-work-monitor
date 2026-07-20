from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Document
from app.db.models import Action
from app.db.models import Risk

router = APIRouter()


@router.get("")
def get_dashboard():

    db = SessionLocal()

    documents = db.scalars(select(Document)).all()
    actions = db.scalars(select(Action)).all()
    risks = db.scalars(select(Risk)).all()

    return {
        "documents": len(documents),
        "actions_open": len(actions),
        "risks_open": len(risks),
        "system_status": "healthy"
    }