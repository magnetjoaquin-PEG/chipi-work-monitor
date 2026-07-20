from pydantic import BaseModel


class RiskCreate(BaseModel):
    title: str
    description: str
    severity: str
    source: str