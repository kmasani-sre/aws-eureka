""" Base interface for AWSCloud actions """
import boto3
from botocore.exceptions import NoCredentialsError


class BaseClass:
    boto3_handle = None

    def __init__(self, service, region_name):
        """ Initialize the class """
        self.region = region_name
        self.service = service

        if BaseClass.boto3_handle is None:
            BaseClass.boto3_handle = self.connect

        self.connection = BaseClass.boto3_handle

    @property
    def connect(self):
        """ Establish connection to AWS Service """

        try:
            client = boto3.client(self.service,
                                  region_name=self.region)
        except NoCredentialsError():
            print('ERR: Please ensure you have Role attached or authentication details are specified')
            raise
        except Exception as e:
            print("ERR: Problem connecting to AWS Service" + str(e))
            raise
        return client
