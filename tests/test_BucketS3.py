import boto3
from moto import mock_s3
from src.exemplo3 import BucketS3
import pytest


class TestS3:
    @pytest.fixture
    @mock_s3
    def resources_aws(self):
        conn = boto3.resource('s3', region_name='us-east-1')
        return conn

    @mock_s3
    def test_retornar_um_bucket_criado(self, resources_aws):
        BucketS3('Dados')
        assert resources_aws.Bucket('Dados') in resources_aws.buckets.all()

    @mock_s3
    def test_my_model_save(self, resources_aws):
        bucket = BucketS3('Dados')
        bucket.save('clodonil', 'eh show')

        body = resources_aws.Object('Dados', 'clodonil')
        msg = body.get()['Body'].read().decode("utf-8")

        assert msg == 'eh show'
