from pydantic import BaseModel


class DocumentCreate(BaseModel):
    name: str
    path: str


class DocumentResponse(BaseModel):
    id: int
    name: str
    path: str
    status: str
