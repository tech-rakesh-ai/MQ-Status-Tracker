from datetime import datetime, timedelta

from fastapi import Query, APIRouter
from typing import List
from apps.tracker import services
from apps.tracker.schemas import StatusCountResponse

router = APIRouter(
    prefix="/tracker",
    tags=["Tracker"]
)


@router.get('/status_count', response_model=List[StatusCountResponse])
async def status_count(
        start: str = Query((datetime.utcnow() - timedelta(days=1)).isoformat()),
        end: str = Query(datetime.utcnow().isoformat())
):
    """
    :param start: start date
    :param end: end date
    :return: list of status counts
    """
    return await services.status_count(start, end)
