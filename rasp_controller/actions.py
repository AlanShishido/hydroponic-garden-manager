import os
import time

from pyfase import MicroService
from PyfaseActionBase.pyfaceBase import ActionBase
from rasp_controller import methods

class SystemBase(ActionBase):
    def __init__(self):
        super(SystemBase, self).__init__()

    @staticmethod
    def create_sample_model():
        return{
            'type': 'sample',
            'tank': {
                'ph_value': 0,
                'tds_value': 0,
                't_value': 0
            }
        }


class HydroponicSystem(SystemBase):
    def __init__(self):
        super(HydroponicSystem, self).__init__()

    def on_connect(self):
        print('## ON_CONNECT ## {}'.format(self.name))

    @MicroService.action
    def console_log(self, service, data):
        print('service: {} \ndata:{}'.format(service, data))

    @MicroService.action
    def get_sample(self, service, data):
        payload = self.create_sample_model()
        print(payload['tank'])
        self.request_action('get_ph_value', payload)

    @MicroService.action
    def get_ph_value(self, service, data):
        ph_data = methods.get_ph_simulate()  # Colocando pra Simular a aquisição do valor
        # self.request_action('save_ph_value', {'ph_value': ph_data})
        tank = data['tank']
        tank['ph_value'] = ph_data
        data['tank'] = tank
        print(data['tank'])

        self.request_action('get_tds_value', data)

    @MicroService.action
    def get_tds_value(self, service, data):
        tds_value = methods.get_tds_simulate()
        tank = data['tank']
        tank['tds_value'] = tds_value
        data['tank'] = tank
        print(data['tank'])

    @MicroService.task
    def data_acquisition(self):
        while True:
            self.request_action('get_sample', {})  # próprio HydroponicSystem
            time.sleep(int(os.environ.get('INTERVAL_TASK')))
