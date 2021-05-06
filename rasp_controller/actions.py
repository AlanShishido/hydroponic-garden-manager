import os
import time
import random

from pyfase import MicroService
from PyfaseActionBase.pyfaceBase import ActionBase


class HydroponicSystem(ActionBase):
    def __init__(self):
        super(HydroponicSystem, self).__init__()

    def on_connect(self):
        print('## ON_CONNECT ## {}'.format(self.name))

    @MicroService.action
    def console_log(self, service, data):
        print('service: {} \ndata:{}'.format(service,data))

    @MicroService.action
    def get_ph_value(self, service, data):
        ph_data = random.randrange(10, 50, 1) #Colocando pra Simular a aquisição do valor
        self.request_action('save_ph_value', {'ph_value':ph_data})


    @MicroService.task
    def data_acquisition(self):
        while True:
            self.request_action('get_ph_value', {})
            time.sleep(int(os.environ.get('INTERVAL_TASK')))

