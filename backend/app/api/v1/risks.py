from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Risk
from app.modules.risks.schemas import RiskCreate

router = APIRouter()


@router.get("")
def get_risks():

    db = SessionLocal()

    risks = db.scalars(
        select(Risk)
    ).all()

    return {
        "total": len(risks),
        "risks": [
            {
                "id": r.id,
                "title": r.title,
                "description": r.description,
                "severity": r.severity,
                "status": r.status,
                "source": r.source
            }
            for r in risks
        ]
    }


@router.post("")
def create_risk(risk: RiskCreate):

    db = SessionLocal()

    new_risk = Risk(
        title=risk.title,
        description=risk.description,
        severity=risk.severity,
        status="OPEN",
        source=risk.source
    )

    db.add(new_risk)
    db.commit()
    db.refresh(new_risk)

    return {
        "id": new_risk.id,
        "status": "created"
    }
