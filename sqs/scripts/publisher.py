import argparse
from AWSCloud.SQS import SQS
import json

MESSAGES_DATAFILE = "data/message.json"
NUMBER_OF_MESSAGES = 1  # Default message count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Helps in publishing messages to SQS Queue")
    parser.add_argument("--queue_name", "-q", action="store", required=True, help="AWS Queue Name")
    parser.add_argument("--count", "-c", action="store", required=False, help="Number of messages to send")

    args = parser.parse_args()

    sqs_object = SQS()

    queue_url = sqs_object.get_queue_url(args.queue_name)
    if queue_url is not None:
        print(f"Queue URL: {queue_url}")
        print(f"Publishing message to Queue  ..")
        with open(MESSAGES_DATAFILE, 'r') as INPUT_FILE:
            data = json.load(INPUT_FILE)

        if args.count is not None:
            NUMBER_OF_MESSAGES = int(args.count)

        messages = data.get('messages')
        index_pt = 0
        while index_pt < NUMBER_OF_MESSAGES:
            attributes = messages[index_pt].get('attributes')
            payload = messages[index_pt].get('payload')
            message_id = sqs_object.send_message(queue_url, attributes, payload)
            print(f"Message [{index_pt}] Sent. Message-ID: {message_id}")
            index_pt += 1
    else:
        print(f"Aborting the run as Queue URL for {args.queue_name} cannot be located.")
