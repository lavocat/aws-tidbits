#!/usr/bin/python3

import requests
import os
import boto3


def get_boto_session():
    if os.getenv("AWS_CONTAINER_CREDENTIALS_RELATIVE_URI", None) is None:
        return boto3.Session()  # This is for running local
    uri = "http://169.254.170.2" + os.getenv("AWS_CONTAINER_CREDENTIALS_RELATIVE_URI")
    aws = requests.get(uri).json
    return boto3.Session(aws_access_key_id=aws['AwsAccessKey'],
                         aws_secret_access_key=aws['SecretAccessKey'],
                         aws_session_token=aws['Token'])
