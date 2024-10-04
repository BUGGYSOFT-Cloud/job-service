from typing import Any
from fastapi import HTTPException

from framework.resources.base_resource import BaseResource

from app.models.job import JobInfo
from app.services.service_factory import ServiceFactory


class JobResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        # TODO -- Replace with dependency injection.
        #
        self.data_service = ServiceFactory.get_service("JobResourceDataService")
        self.database = "jobs"
        self.collection = "JobInfo"
        self.key_field="job_id"

    def get_by_key(self, key: int) -> JobInfo:

        d_service = self.data_service

        result = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )

        if result is None:
            raise HTTPException(status_code=404, detail="Item not found!")
        else:
            print("DEBUG:\tretrieved job {}".format(result))

        result = JobInfo(**result)
        return result

    def get_all_by_field(self, field: str, value: Any) -> [JobInfo]:
        d_service = self.data_service

        result = d_service.get_all_data_object(
            self.database, self.collection, key_field=field, key_value=value
        )

        if result is None or len(result) == 0:
            raise HTTPException(status_code=404, detail="Item not found!")
        else:
            print("DEBUG:\tretrieved {} items".format(len(result)))

        result = [JobInfo(**item) for item in result]
        return result

