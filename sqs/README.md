## SQS
Amazon Simple Queue Service (SQS) is a managed service that lets you send, store and receive messages. 
It helps in building de-coupled architecture.

Size of each message by default is 1 byte and maximum can be of 256KB. However if you have a requirement of sending
messages higher size than that then you can leverage S3 as the data-store for these messages. In this setup, you can 
have maximum message size of 2GB.

## SQS Queue Types
### Standard Queues
Standard queues are fast but at the same time they do not offer any gaurantee about the order in which messages are sent out.
But they do guarantee atleast-once delivery of the message.
Maximum number of in-flight messages is 120K

### FIFO Queues
FIFO queues are slow when compared to Standard queues - this can be related to additional overhead of ensuring that the 
order of messages is maintained. These queues always sends only 1 message.
Maximum number of in-flight messages is 20K.