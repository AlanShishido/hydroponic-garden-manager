import os
import logging
from os.path import exists

from django.db import DatabaseError, transaction
from dotenv import load_dotenv
from pyfase import MicroService


class ActionBase(MicroService):
    def __init__(self):
        self.sender, self.receiver = self.__load_conf()
        print('Sender: {}  === Receiver: {}'.format(self.sender, self.receiver))
        self.message = None
        self.except_message = None
        self.websocket = None
        super(ActionBase, self).__init__(self, sender_endpoint=self.sender, receiver_endpoint=self.receiver)

    def on_connect(self):
        logging.warning(msg="### ON CONNECT "+ self.name)

    @staticmethod
    def __load_conf():
        endpoint = 'tcp://{host}:{port}'
        base_dir = os.path.dirname(
            os.path.abspath(__file__)
        )
        microservice = os.path.join(base_dir, '../hydroponic.conf')
        if exists(microservice):
            load_dotenv(microservice)
            sender_endpoint = endpoint.format(host=os.environ.get('PYFASE_HOST'), port=os.environ.get('PYFASE_SENDER_PORT'))
            receiver_endpoint = endpoint.format(host=os.environ.get('PYFASE_HOST'), port=os.environ.get('PYFASE_RECEIVER_PORT'))
            return sender_endpoint, receiver_endpoint
        else:
            return endpoint.format('localhost', '3000'), endpoint.format('localhost', '9000')

    @staticmethod
    def run_methods(action, payload):
        try:
            with transaction.atomic():
                action(payload)
                return
        except (DatabaseError, Exception) as Ex:
            transaction.rollback()
            return Ex

