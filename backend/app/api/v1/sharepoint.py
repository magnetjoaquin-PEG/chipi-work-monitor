from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
def sharepoint_status():
    return {
        "status": "pending-approval",
        "site": "Generacionelica",
        "connector": "graph"
    }