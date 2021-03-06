import logging
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
                'ph_value': -1.0,
                'tds_value': -1.0,
                't_value': -1.0
            }
        }


class HydroponicSystem(SystemBase):
    def __init__(self):
        self.setup_rasp_gpio()
        super(HydroponicSystem, self).__init__()

    @staticmethod
    def setup_rasp_gpio():
        pass
        # methods.setup_gpio_pins()

    def on_connect(self):
        print('## ON_CONNECT ## {}'.format(self.name))

    @MicroService.action
    def get_sample(self, service, data):
        payload = data
        tank_value = payload['tank']
        try:
            tank_value['ph_value'] = methods.get_ph_simulate()
            tank_value['tds_value'] = methods.get_tds_simulate()
            tank_value['t_value'] = methods.get_temperature_simulate()
            print(tank_value)
            self.request_action('save_nutrients_value', tank_value)
        except Exception as Ex:
            logging.warning(msg=Ex)

        self.request_action('save_nutrients_value', tank_value)

    @MicroService.action
    def get_ph_value(self, service, data):
        payload = data
        ph_data = methods.pi_get_ph(10)
        tank = payload['tank']
        tank['ph_value'] = ph_data
        payload['tank'] = tank
        print(payload)

    @MicroService.action
    def get_tds_value(self, service, data):
        payload = data
        tds_value = methods.get_tds_simulate()
        tank = payload['tank']
        tank['tds_value'] = tds_value
        payload['tank'] = tank
        print(payload['tank'])

    @MicroService.action
    def get_temperature_value(self, service, data):
        payload = data
        temperature_value = methods.get_temperature_simulate()
        t_value = payload['tank']
        t_value['t_value'] = temperature_value
        payload['tank'] = t_value
        print(payload['tank'])

    @MicroService.task
    def data_acquisition(self):
        while True:
            payload = self.create_sample_model()
            self.request_action('get_sample', payload)  # próprio HydroponicSystem
            time.sleep(int(os.environ.get('INTERVAL_TASK')))



