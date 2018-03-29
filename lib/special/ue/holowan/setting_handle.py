# coding=utf-8

from setting_config import *
import requests


def create_path(path_id, path_name):
    """
    create a path
    """
    url = URL_PREFIX + '/emulator_config'
    data = setting_path_config(modify_switch=2, engine_id=1, path_id=path_id, path_name=path_name)
    response = requests.post(url=url, headers=HEADERS, data=data)
    print response.status_code
    print response.text


def delete_path(path_id, path_name):
    """
    delete a path
    """
    url = URL_PREFIX + '/emulator_config'
    data = setting_path_config(modify_switch=1, engine_id=ENGINE_ID, path_id=path_id, path_name=path_name)
    response = requests.post(url=url, headers=HEADERS, data=data)
    print response.status_code
    print response.text


def start_path(path_id, path_name):
    """
    启动指定path
    """
    url = URL_PREFIX + '/emulator_config'
    data = setting_path_config(modify_switch=3, engine_id=ENGINE_ID, path_id=path_id, path_name=path_name, if_enable=2)
    response = requests.post(url=url, headers=HEADERS, data=data)
    print response.status_code
    print response.text


def stop_path(path_id, path_name):
    """
    停止指定path
    """
    url = URL_PREFIX + '/emulator_config'
    data = setting_path_config(modify_switch=3, engine_id=ENGINE_ID, path_id=path_id, path_name=path_name, if_enable=1)
    response = requests.post(url=url, headers=HEADERS, data=data)
    print response.status_code
    print response.text


def setting_path_params(path_id, path_name, path_director=3,
                        pltr_bandwidth_rate=1000, pltr_delay_co_devalue=0, pltr_loss_random_rate=0,
                        prtl_bandwidth_rate=1000, prtl_delay_co_devalue=0, prtl_loss_random_rate=0,
                        pltr_background_switch=1, pltr_background_rate=0, pltr_background_burst=0,
                        prtl_background_switch=1, prtl_background_rate=0, prtl_background_burst=0):
    """
    设定指定path的规则参数
    """

    url = URL_PREFIX + '/emulator_config'
    data = setting_path_params_config(engine_id=ENGINE_ID, path_id=path_id, path_name=path_name,
                                      path_director=path_director,
                                      pltr_delay_co_devalue=pltr_delay_co_devalue,
                                      pltr_loss_random_rate=pltr_loss_random_rate,
                                      pltr_bandwidth_rate=pltr_bandwidth_rate,
                                      prtl_bandwidth_rate=prtl_bandwidth_rate,
                                      prtl_loss_random_rate=prtl_loss_random_rate,
                                      prtl_delay_co_devalue=prtl_delay_co_devalue,
                                      pltr_background_switch=pltr_background_switch,
                                      pltr_background_rate=pltr_background_rate,
                                      pltr_background_burst=pltr_background_burst,
                                      prtl_background_switch=prtl_background_switch,
                                      prtl_background_rate=prtl_background_rate,
                                      prtl_background_burst=prtl_background_burst
                                      )

    response = requests.post(url=url, headers=HEADERS, data=data)
    print response.status_code
    print response.text


def setting_packet_classifier(src_ip, dst_ip, path_id):
    """
    设定包分类器，哪些包适应哪个path的规则
    """
    url = URL_PREFIX + '/emulator_config'
    data = setting_packet_classifier_config(src_ip=src_ip, dst_ip=dst_ip, path_id=path_id)

    response = requests.post(url=url, headers=HEADERS, data=data)
    print response.status_code
    print response.text


if __name__ == '__main__':
    # create_path(path_id=11, path_name="test_create_path1")
    # start_path(path_id=11, path_name="test_create_path1")
    # create_path(path_id=12, path_name="free_path")
    # start_path(path_id=12, path_name="free_path")
    # stop_path(path_id=11, path_name="test_create_path1")
    # delete_path(path_id=11, path_name="test_create_path1")

    # setting_path_params(path_id=11, path_name='test_create_path1', path_director=3,
    #                     pltr_delay_co_devalue=123, pltr_loss_random_rate=10, pltr_bandwidth_rate=2,
    #                     prtl_bandwidth_rate=2, prtl_loss_random_rate=5, prtl_delay_co_devalue=321)
    # setting_path_params(path_id=12, path_name='free_path', path_director=3,
    #                     pltr_delay_co_devalue=0, pltr_loss_random_rate=0, pltr_bandwidth_rate=1000,
    #                     prtl_bandwidth_rate=1000, prtl_loss_random_rate=0, prtl_delay_co_devalue=0)

    # setting_packet_classifier(src_ip='192.168.8.41', dst_ip='192.168.8.45', path_id=11)

    pass

