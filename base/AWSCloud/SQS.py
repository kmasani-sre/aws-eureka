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

    def send_message(self, queue_url, message_attributes, message_body):

        try:
            self.connection.send_message(QueueUrl=queue_url, MessageAttributes=message_attributes, MessageBody=message_body)

        except botocore.exceptions.ClientError as err:
            if err.response['Error']['Code'] == 'InternalError':
                print('Error Message: {}'.format(err.response['Error']['Message']))
                print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
                print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
            else:
                raise err

    def receive_message(self, queue_url):
        # Receive message from SQS queue
        response = self.connection.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )

        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

    def delete_message_in_queue(self, queue_url, receipt_handle):
        # Delete received message from queue
        self.connection.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print('Deleted the message')
