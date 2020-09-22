import os
import json

import boto3


def get_aws_config():
    try:
        with open('../aws_config.json', 'r') as stream:
            # TODO: change to use BASEDIR
            config = json.load(stream)
    except FileNotFoundError as e:
        return f'ERROR: {e}'
    return config


def make_session():
    # TODO: stub: make_session()
    return


def launch_ec2_instance(params):
    # TODO: stub: launch_ec2_instance(params)
    return


def terminate_ec2_instance(params):
    # TODO: stub: terminate_ec2_instance(params)
    return


def get_running_ec2_instance(params):
    # TODO: stub: get_running_ec2_instance(params)
    return


my_conf = get_aws_config()
print(my_conf)
