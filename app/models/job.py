from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class JobInfo(BaseModel):
    job_id: Optional[int] = None
    job_name: Optional[str] = None
    job_company: Optional[str] = None
    job_created_at: Optional[str] = None
    job_url: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "job_id": 204283,
                "job_name": "Software Development Engineer I",
                "job_company": "Amazon AWS",
                "job_created_at": "May 21, 2024",
                "job_url": "https://www.amazon.jobs/en/jobs/2748536/software-development-engineer-i?cmpid=SPLICX0248M&utm_source=linkedin.com&utm_campaign=cxro&utm_medium=social_media&utm_content=job_posting&ss=paid"
            }
        }
