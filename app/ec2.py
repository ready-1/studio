import os
import json
from pprint import pprint

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


def launch_ec2_instance(params):
    # TODO: stub: launch_ec2_instance(params)
    return


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


# params = {}
# filters = [{"Name": "tag:Organization", "Values": ["Ready-1"]}]
# dry_run = False
# pagination_config = {"MaxItems": 20, "PageSize": 20}
# page_iterator = get_ec2_instances(filters, dry_run, pagination_config)
page_iterator = get_ec2_instances()
for page in page_iterator:
    pprint(page, indent=1)
