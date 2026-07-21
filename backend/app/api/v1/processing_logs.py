from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_processing_logs():

    return {
        "total": 0,
        "logs": []
    }