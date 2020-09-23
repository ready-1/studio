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
