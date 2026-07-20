from fastapi import APIRouter

from app.api.v1.sharepoint import router as sharepoint_router
from app.api.v1.documents import router as documents_router
from app.api.v1.actions import router as actions_router
from app.api.v1.risks import router as risks_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.agenda import router as agenda_router

router = APIRouter()

router.include_router(
    sharepoint_router,
    prefix="/api/v1/sharepoint",
    tags=["sharepoint"]
)

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



