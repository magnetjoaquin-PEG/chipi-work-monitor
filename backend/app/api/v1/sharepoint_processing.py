from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ProcessDocumentRequest(BaseModel):
    name: str


@router.post("/process-document")
def process_document(request: ProcessDocumentRequest):

    return {
        "document": request.name,
        "status": "processed"
    }