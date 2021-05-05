import logging

from pyfase import MicroService
from PyfaseActionBase.pyfaceBase import ActionBase


class HydroponicStateMachine(ActionBase):
    
    def __init__(self):
        super(HydroponicStateMachine, self).__init__()

    def on_connect(self):
        print('testando')

    @MicroService.actions
    def save_data_rasp(self, service, data):
        logging.warning(msg='saving rasp data')
