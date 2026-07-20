from fastapi import APIRouter
from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import Document
from app.modules.documents.schemas import DocumentCreate

router = APIRouter()


@router.get("")
def get_documents():

    db = SessionLocal()

    documents = db.scalars(
        select(Document)
    ).all()

    return {
        "total": len(documents),
        "documents": [
            {
                "id": d.id,
                "name": d.name,
                "path": d.path,
                "status": d.status
            }
            for d in documents
        ]
    }


@router.post("")
def create_document(document: DocumentCreate):

    db = SessionLocal()

    new_document = Document(
        name=document.name,
        path=document.path,
        status="ACTIVE"
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return {
        "id": new_document.id,
        "status": "created"
    }