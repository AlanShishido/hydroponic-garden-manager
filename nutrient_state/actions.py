from nutrient_state import methods
from pyfase import MicroService
from PyfaseActionBase.pyfaceBase import ActionBase


class NutrientsDatabase(ActionBase):
    def __init__(self):
        super(NutrientsDatabase, self).__init__()

    @MicroService.action
    def save_nutrients_value(self, service, data):

        payload = (data['ph_value'], data['tds_value'], data['t_value'])
        result = self.run_methods(methods.save_nutrients_value, payload)
        if result is None:
            print('saved')
        else:
            print(result)
