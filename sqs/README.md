## SQS
Amazon Simple Queue Service (SQS) is a managed service that lets you send, store and receive messages. 
It helps in building de-coupled architecture.

Size of each message by default is 1 byte and maximum can be of 256KB. However if you have a requirement of sending
messages higher size than that then you can leverage S3 as the data-store for these messages. In this setup, you can 
have maximum message size of 2GB.

## SQS Queue Types
### Standard Queues
Standard queues are fast but at the same time they do not offer any gaurantee about the order in which messages are sent out.
They do guarantee atleast-once delivery of the message.
Maximum number of in-flight messages is 120K

### FIFO Queues
FIFO queues maintain the order of messages. They are slow when compared to Standard queues - this can be attributed to 
additional overhead of ensuring that the order of messages is maintained. 
These queues do not introduce any duplicate messages and does exactly-once processing of a given message.
Maximum number of in-flight messages is 20K.

## SQS Visibility Timeout
When a message is read by a consumer, it is not immediately deleted instead, it still lives in the message queue. Because SQS
is a distributed system, there is no guarantee that consumer has received the message or has processed the message successfully.
To ensure that messages are not lost, consumers must delete the message from SQS queue once it is successfully processed.
But if the message resides in the Queue, then there is a chance that other consumers may also start processing the same message.
To ensure that the message is not read by other consumers, there is a configuration option called 'Visibility Timeout'
Default visibility timeout: 30 seconds. Minimum is 0 seconds and maximum is 12 hours.
By setting appropriate visibility-timeout value, SQS ensures that the message is not made available for other consumers immediately and 
the first consumer who processes the message successfully will delete the message at the end of the transaction.

In an event of first consumer crashing before the message is deleted from the Queue, then on visibility-timeout expiry, message
is made available for all consumers again.

Note: Always ensure that you set visibility timeout to match execution time of your business logic. This ensures that the message
is not made available for multiple consumers.