import boto3
from moto import mock_sqs
from src.exemplo3 import SqsFila
import pytest


class TestSqs:
    @mock_sqs
    def test_deve_publicar_um_elemento_na_fila(self):
        sqs = boto3.resource('sqs', region_name='us-east-1')
        sqs.create_queue(QueueName='test', Attributes={
            'DelaySeconds': '1'})

        fb = SqsFila(sqs)
        retorno = fb.sqs_send('test', {"chave": "valor"})

        conn = sqs.get_queue_by_name(QueueName='test')
        messages = conn.receive_messages(MaxNumberOfMessages=1,
                                         AttributeNames=['All'],
                                         WaitTimeSeconds=5)

        print(retorno)
        assert retorno['ResponseMetadata']['HTTPStatusCode'] == 200
        assert messages[0].body == '{"chave": "valor"}'

    @mock_sqs
    def test_deve_recuperar_um_object_salvo_na_fila(self):
        sqs = boto3.resource('sqs', region_name='us-east-1')
        sqs.create_queue(QueueName='test', Attributes={
            'DelaySeconds': '1'})

        conn = sqs.get_queue_by_name(QueueName='test')
        conn.send_message(MessageBody='{"nome":"clodonil"}')

        fb = SqsFila(sqs)
        retorno = fb.sqs_receive('test')

        print(retorno[0].body)
        assert retorno[0].body != '{"nome": "clodonil"}'
