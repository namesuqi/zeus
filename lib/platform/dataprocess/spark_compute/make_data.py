from lib.platform.dataprocess.spark_compute.makedata.qos_buffering_count import *
from lib.platform.dataprocess.spark_compute.makedata.qos_startup import *
from lib.platform.dataprocess.spark_compute.makedata.bd_flow import *
from lib.platform.dataprocess.spark_compute.makedata.download_flow import *
from lib.platform.dataprocess.spark_compute.makedata.upload_flow import *


def make_data(task_name, hour=''):
    task_object = eval(task_name + '()')
    task_object.make_data(hour)

if __name__ == '__main__':
    # make_data('QosStartUp', 15)
    make_data('DownloadFlow', 23)
