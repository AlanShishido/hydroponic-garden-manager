
from pyfase import Fase

VERSION = '1.0'

def init_core(sender_port: int, receiver_port: int):
    try:
        sender = 'tcp://*:{}'.format(sender_port)
        receiver = 'tcp://*:{}'.format(receiver_port)
        print('\n')
        print('Server de sender e receiver: {} e {}'.format(sender_port, receiver_port))
        print('\n')
        Fase(sender_endpoint=sender, receiver_endpoint=receiver)
    except Exception as Ex:
        print('connection failed: {}'.format(Ex))