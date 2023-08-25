""" Base interface for AWSCloud actions """
import boto3
from botocore.exceptions import NoCredentialsError


class AWSCloud:
    def __init__(self, service, **kwargs):
        """ Initialize the class """
        self.region = kwargs.get('region_name')
        self.service = service
        self.boto3_conn = self.connect()

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
