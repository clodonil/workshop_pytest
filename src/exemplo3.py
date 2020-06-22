import boto3
import json


class BucketS3:
    def __init__(self, bucketname):
        self._bucketname = bucketname
        self.conn = boto3.client('s3', region_name='us-east-1')
        self.conn.create_bucket(Bucket=self._bucketname)

    def save(self, name, value):
        self.conn.put_object(Bucket=self._bucketname, Key=name, Body=value)


class SqsFila:
    def __init__(self, sqs):
        self.sqs = boto3.resource('sqs', region_name='us-east-1')

    def sqs_receive(self, fila):
        """
        recupera templates da lista
        """

        conn = self.sqs.get_queue_by_name(QueueName=fila)
        messages = conn.receive_messages(MaxNumberOfMessages=10,
                                         AttributeNames=['All'],
                                         WaitTimeSeconds=1)
        return messages

    def sqs_send(self, fila, msg):
        """
         envia mensagem para lista
        """
        conn = self.sqs.get_queue_by_name(QueueName=fila)
        return conn.send_message(MessageBody=json.dumps(msg))

    def sqs_delete(self, event):
        """
        deletando mensagem da fila
        """
        retorno = event.delete()
        if retorno['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
