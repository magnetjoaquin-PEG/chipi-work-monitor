from fastapi import APIRouter

from app.modules.sharepoint.service import (
    SharePointService
)

router = APIRouter()


@router.get("/status")
def sharepoint_status():

    return SharePointService.get_status()


@router.get("/inventory")
def sharepoint_inventory():

    return SharePointService.get_inventory()