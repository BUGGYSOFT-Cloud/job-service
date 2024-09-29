from fastapi import APIRouter

from app.models.job import JobInfo
from app.resources.job_resource import JobResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/job_info/{job_id}", response_model=JobInfo, tags=["users"])
async def get_job(job_id: int) -> JobInfo:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("JobResource")
    result = res.get_by_key(job_id)
    return result

@router.get("/jobs_of_company/{company_name}", response_model=list[JobInfo], tags=["users"])
async def get_job_by_company(company_name: str) -> list[JobInfo]:
        res = ServiceFactory.get_service("JobResource")
        result = res.get_all_by_field("job_company", company_name)
        return result
