#!/usr/bin/python3

import boto3
from boto_session import get_boto_session


def get_instances():
    session = get_boto_session()
    ec2 = session.client('ec2')
    filters = [
        # Get running instances
        {'Name': 'instance-state-name', 'Values': ['running']},
        ]
    response = ec2.describe_instances(Filters=filters)
    instance_list = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            for network_interface in instance["NetworkInterfaces"]:
                instance_list.append(instance["PrivateIpAddress"])
    return instance_list  # Returns list object with PrivateIPAddress
