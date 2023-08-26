import argparse
from AWSCloud.SQS import SQS

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Helps in publishing messages to SQS Queue")
    parser.add_argument("--queue_name", "-q", action="store", required=True)

    args = parser.parse_args()

    sqs_object = SQS()

    queue_url = sqs_object.get_queue_url(args.queue_name)
    if queue_url is not None:
        print(f"Queue URL: {queue_url}")
    else:
        print(f"Aborting the run as Queue URL for {args.queue_name} cannot be located.")
