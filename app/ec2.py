import os
import json
from pprint import pprint
import datetime

import boto3
import botocore.exceptions


def get_aws_config():
    try:
        with open('../aws_config.json', 'r') as stream:
            # TODO: change to use BASEDIR
            config = json.load(stream)
    except FileNotFoundError as e:
        return f'ERROR: {e}'
    return config


def make_session():
    try:
        config = get_aws_config()
        new_session = boto3.session.Session(
            aws_access_key_id=config["aws_access_key_id"],
            aws_secret_access_key=config["aws_secret_access_key"],)
        return new_session
    except Exception as e:
        return e


def launch_ec2_instances(params):
    """Launch EC2 instances with given parameters

    Returns:
        response (list): List of ec2 instance objects
    Args:
        params (dict): Per specification at https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html?highlight=create_instances#EC2.ServiceResource.create_instances

        {
        "ImageId": 'string',
        "InstanceType": 'string',
        "MaxCount": 1,
        "MinCount": 1,
        "Monitoring": {
            'Enabled': False
        },
        "SecurityGroupIds": [
            'string',
        ],
        "SubnetId": 'string',
        "DryRun": False,
        "EbsOptimized": False,
        "InstanceInitiatedShutdownBehavior": 'stop',
        "TagSpecifications": [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Studio-1A Linux Tiny'},
                    {'Key': 'Job', 'Value': 'Testing'},
                    {'Key': 'Organization', 'Value': 'Ready-1'},
                    {'Key': 'Studio', 'Value': 'Studio-1A'},
                    {'Key': 'Purpose', 'Value': 'Testing'},
                ]
            },
        ],
    }
    """

    try:
        session = make_session()
        ec2_connection = session.resource('ec2')
        # launch instance
        response = ec2_connection.create_instances(**params)
    except FileNotFoundError as error:
        return f'ERROR: {error}'
    except botocore.exceptions.ClientError as error:
        return f'ERROR: {error}'
    return response


def get_ec2_instances(filters=[], dry_run=False, pagination_config={"MaxItems": 20, "PageSize": 20}, **kwargs):
    try:
        session = make_session()
        client = session.client('ec2')
        paginator = client.get_paginator('describe_instances')
        response_iterator = paginator.paginate(
            Filters=filters,
            DryRun=dry_run,
            PaginationConfig=pagination_config
        )
    except botocore.exceptions.ParamValidationError as error:
        raise ValueError(
            'The parameters you provided are incorrect: {}'.format(error))
    except botocore.exceptions.ClientError as error:
        raise error

    return response_iterator


def terminate_ec2_instance(params):
    # TODO: stub: terminate_ec2_instance(params)
    return


# configure instance_params
instance_params = {
    "ImageId": 'ami-00514a528eadbc95b',
    "InstanceType": 't2.micro',
    "MaxCount": 1,
    "MinCount": 1,
    "Monitoring": {
        'Enabled': False
    },
    "SecurityGroupIds": [
        'sg-0e87825359f9b21ff',
    ],
    "SubnetId": 'subnet-08a94fe90f894ef3b',
    "DryRun": False,
    "EbsOptimized": False,
    "InstanceInitiatedShutdownBehavior": 'stop',
    "TagSpecifications": [
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'Studio-1A Linux Tiny'},
                {'Key': 'Job', 'Value': 'Testing'},
                {'Key': 'Organization', 'Value': 'Ready-1'},
                {'Key': 'Studio', 'Value': 'Studio-1A'},
                {'Key': 'Purpose', 'Value': 'Testing'},
            ]
        },
    ],
}

result = launch_ec2_instances(instance_params)
# pprint(result[0].tags[0]["Value"])
pprint(result)
