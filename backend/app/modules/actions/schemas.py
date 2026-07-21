from pydantic import BaseModel


class ActionCreate(BaseModel):
    title: str
    description: str
    priority: str


class ActionResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str

class ActionUpdate(BaseModel):
    status: str
