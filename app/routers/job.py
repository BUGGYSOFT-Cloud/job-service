from fastapi import APIRouter

from app.models.job import JobInfo
from app.resources.job_resource import JobResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/job_info/{job_id}", tags=["users"])
async def get_job(job_id: int) -> JobInfo:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("JobResource")
    result = res.get_by_key(job_id)
    return result