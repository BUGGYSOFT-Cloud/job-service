from framework.services.service_factory import BaseServiceFactory
import app.resources.job_resource as job_resource
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService


# TODO -- Implement this class
class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):
        #
        # TODO -- The terrible, hardcoding and hacking continues.
        #
        if service_name == 'JobResource':
            result = job_resource.JobResource(config=None)
        elif service_name == 'JobResourceDataService':
            context = dict(user="root", password="",
                           host="35.184.107.37", port=3306)
            data_service = MySQLRDBDataService(context=context)
            result = data_service
        else:
            result = None

        return result




