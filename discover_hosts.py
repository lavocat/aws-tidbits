#!/usr/bin/python3

import boto3
from aws-tidbits import get_boto_session


def get_instances_by_tag():
    session = get_boto_session()
    ec2 = session.client('ec2')
    filters = [{  # filter for running instances with specific tag
        'Name': 'instance-state-name', 'Values': ['running'],
        'Name': 'tag:Application', 'Values': ['application_name'],
        }]
    response = ec2.describe_instances(Filters=filters)
    instance_list = []
    # Get private IP addresses from response
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            for network_interface in instance["NetworkInterfaces"]:
                instance_list.append(instance["PrivateIpAddress"])
    return instance_list
