import pytest

import ec2


def test_get_aws_config():
    conf = ec2.get_aws_config()
    assert "aws_access_key_id" in conf.keys()


def test_make_session():
    session = ec2.make_session()
    assert session.region_name == 'us-east-1'


def test_get_ec2_instances():
    page_iterator = ec2.get_ec2_instances()
    pages = []
    for page in page_iterator:
        pages.append(page)
    assert pages[0]["ResponseMetadata"]["HTTPStatusCode"] == 200

    # TODO: add better tests for get_ec2_instances()


def test_launch_ec2_instance():
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
        "DryRun": True,
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

    result = ec2.launch_ec2_instances(instance_params)

    assert 'Request would have succeeded, but DryRun flag is set.' in result
