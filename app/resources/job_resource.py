from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.job import JobInfo
from app.services.service_factory import ServiceFactory


class JobResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        # TODO -- Replace with dependency injection.
        #
        self.data_service = ServiceFactory.get_service("JobResource")
        self.database = "jobs"
        self.collection = "JobInfo"
        self.key_field="job_id"

    def get_by_key(self, key: int) -> JobInfo:

        d_service = self.data_service

        result = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )
        print(result)
        result = JobInfo(**result)
        return result


