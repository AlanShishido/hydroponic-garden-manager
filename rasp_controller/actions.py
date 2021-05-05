import os
import time
from pyfase import MicroService
from PyfaseActionBase.pyfaceBase import ActionBase

class HydroponicBase(ActionBase):

    @MicroService.action
    def console_log(self, service, data):
        print('service: {} \ndata:{}'.format(service,data))

    @MicroService.task
    def tarefa(self):
        print('testando task')
        while True:
            print('printando')
            time.sleep(int(os.environ.get('INTERVAL_TASK')))
