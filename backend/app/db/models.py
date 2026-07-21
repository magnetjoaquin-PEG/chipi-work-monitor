from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    status = Column(String)

from sqlalchemy import Column, Integer, String


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(String)
    status = Column(String)

class Risk(Base):
    __tablename__ = "risks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    severity = Column(String)
    status = Column(String)
    source = Column(String)

class ProcessingLog(Base):
    __tablename__ = "processing_logs"

    id = Column(Integer, primary_key=True)
    document_name = Column(String)
    actions_created = Column(Integer)
    risks_created = Column(Integer)

