from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import select

from app.modules.document_intelligence.service import (
    DocumentIntelligenceService
)

from app.db.database import SessionLocal
from app.db.models import Action
from app.db.models import Risk


router = APIRouter()


class AnalyzeRequest(BaseModel):
    content: str


@router.post("/analyze")
def analyze_document(request: AnalyzeRequest):

    return DocumentIntelligenceService.analyze(
        request.content
    )


@router.post("/analyze-and-create")
def analyze_and_create(request: AnalyzeRequest):

    result = DocumentIntelligenceService.analyze(
        request.content
    )

    db = SessionLocal()

    actions_created = 0
    actions_skipped = 0
    risks_created = 0
    risks_skipped = 0

    for action in result["actions_detected"]:

        existing_action = db.scalars(
            select(Action).where(
                Action.title == action["title"]
            )
        ).first()

        if existing_action:
            actions_skipped += 1
            continue

        db_action = Action(
            title=action["title"],
            description="Creada automáticamente por Chipi",
            priority="MEDIUM",
            status="OPEN"
        )

        db.add(db_action)

        actions_created += 1

    for risk in result["risks_detected"]:

        existing_risk = db.scalars(
            select(Risk).where(
                Risk.title == risk["title"]
            )
        ).first()

        if existing_risk:
            risks_skipped += 1
            continue

        db_risk = Risk(
            title=risk["title"],
            description="Creado automáticamente por Chipi",
            severity="HIGH",
            status="OPEN",
            source="Document Intelligence"
        )

        db.add(db_risk)

        risks_created += 1

    db.commit()

    return {
        "actions_created": actions_created,
        "actions_skipped": actions_skipped,
        "risks_created": risks_created,
        "risks_skipped": risks_skipped
    }