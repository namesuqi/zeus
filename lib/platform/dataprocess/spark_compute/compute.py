from lib.platform.dataprocess.spark_compute.computelogic.five_minute_average_startup_delay import *
from lib.platform.dataprocess.spark_compute.computelogic.play_fluency import *
from lib.platform.dataprocess.spark_compute.computelogic.total_flow_hour import *
from lib.platform.dataprocess.spark_compute.computelogic.total_flow_day import *


def compute(task_name, param=''):
    if param == '':
        task_object = eval(task_name + '()')
        task_object.compute()
    else:
        task_object = eval(task_name + '()')
        task_object.compute(param)

if __name__ == '__main__':
    compute('PlayFluency')
