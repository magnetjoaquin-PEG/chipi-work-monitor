from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Action
from app.db.models import ProcessingLog

router = APIRouter()


class AssistantQuestion(BaseModel):
    question: str


@router.post("")
def ask_assistant(
    request: AssistantQuestion
):

    question = request.question.lower()

    db = SessionLocal()

    actions = db.scalars(
        select(Action)
    ).all()

    logs = db.scalars(
        select(ProcessingLog)
    ).all()

    if "acciones abiertas" in question:

        open_actions = [
            a.title
            for a in actions
            if a.status != "DONE"
        ]

        return {
            "answer": (
                f"Hay {len(open_actions)} acciones abiertas."
            ),
            "details": open_actions
        }

    if "acciones completadas" in question:

        done_actions = [
            a.title
            for a in actions
            if a.status == "DONE"
        ]

        return {
            "answer": (
                f"Hay {len(done_actions)} acciones completadas."
            ),
            "details": done_actions
        }

    if "documentos procesados" in question:

        docs = [
            log.document_name
            for log in logs
        ]

        return {
            "answer": (
                f"Se procesaron {len(docs)} documentos."
            ),
            "details": docs
        }

    if "ultimo documento" in question or "último documento" in question:

        if logs:

            return {
                "answer": (
                    f"Último documento procesado: "
                    f"{logs[-1].document_name}"
                ),
                "details": []
            }

    return {
        "answer": "No entendí la consulta.",
        "details": []
    }