from fastapi import APIRouter

from app.api.v1.documents import router as documents_router
from app.api.v1.actions import router as actions_router
from app.api.v1.risks import router as risks_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.agenda import router as agenda_router
from app.api.v1.dashboard_executive import router as executive_router
from app.api.v1.document_intelligence import (
    router as intelligence_router
)
from app.api.v1.sharepoint_inventory import (
    router as sharepoint_inventory_router
)
from app.api.v1.sharepoint_processing import (
    router as sharepoint_processing_router
)
from app.api.v1.processing_logs import (
    router as processing_logs_router
)

router = APIRouter()

router.include_router(
    documents_router,
    prefix="/api/v1/documents",
    tags=["documents"]
)

router.include_router(
    actions_router,
    prefix="/api/v1/actions",
    tags=["actions"]
)

router.include_router(
    risks_router,
    prefix="/api/v1/risks",
    tags=["risks"]
)

router.include_router(
    dashboard_router,
    prefix="/api/v1/dashboard",
    tags=["dashboard"]
)

router.include_router(
    agenda_router,
    prefix="/api/v1/agenda",
    tags=["agenda"]
)

router.include_router(
    executive_router,
    prefix="/api/v1/dashboard/executive",
    tags=["executive-dashboard"]
)

router.include_router(
    intelligence_router,
    prefix="/api/v1/documents",
    tags=["document-intelligence"]
)

router.include_router(
    sharepoint_inventory_router,
    prefix="/api/v1/sharepoint",
    tags=["sharepoint-inventory"]
)

router.include_router(
    sharepoint_processing_router,
    prefix="/api/v1/sharepoint",
    tags=["sharepoint-processing"]
)

router.include_router(
    processing_logs_router,
    prefix="/api/v1/processing-logs",
    tags=["processing-logs"]
)