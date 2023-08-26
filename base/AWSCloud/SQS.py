from AWSCloud.Base import BaseClass
import botocore


class SQS(BaseClass):
    """ Provides functions to interface with SQS Queues """
    def __init__(self, region_name='us-east-1'):
        self._SERVICE_NAME = 'sqs'
        self.region = region_name
        super().__init__(self._SERVICE_NAME, self.region)

    def get_queues(self) -> [str]:
        """ Returns the list of queues in your account """
        print(f"Return the list of {self._SERVICE_NAME} queues .. ")
        try:
            response = self.connection.list_queues()

            response_code = response.get('ResponseMetadata').get('HTTPStatusCode')
            if response_code == 200:
                return response.get('QueueUrls')
            else:
                raise Exception(f"Got unsuccessful response code {response_code} for the query")
        except Exception as e:
            print(f"Exception occurred while querying for SQS queues")
            print(str(e))
            raise

    def get_queue_url(self, queue_name) -> str:
        """ For a given queue, returns its associated Queue-URL"""

        queue_url = None
        try:
            response = self.connection.get_queue_url(
                QueueName=queue_name
            )

            if response.get('ResponseMetadata').get('HTTPStatusCode') == 200:
                queue_url = response.get('QueueUrl')
        except botocore.exceptions.ClientError as error:
            if error.response.get('Error').get('Code') == 'AWS.SimpleQueueService.NonExistentQueue':
                print(f"Please check the provided queue name ({queue_name}) - it cannot be located.")

        return queue_url
