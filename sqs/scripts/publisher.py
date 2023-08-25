import argparse
from pprint import pprint
from AWSCloud.AWSCloud import AWSCloud

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Helps in publishing messages to SQS Queue")
    parser.add_argument("--queue-name", "-q", action="store", required=True)

    args = parser.parse_args()

