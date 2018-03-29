# coding=utf-8
import jenkins
from lib.special.monitor_jenkins.const import *


def get_failed_dateset(server):
    """
    entry function
    :param server:
    :return:
    """
    job_dict = {}
    last_failed_jobs = []
    for job in job_name:
        try:
            tmp_color = server.get_job_info(job)['color']
        except Exception:
            continue
        if u'yellow' in tmp_color or u'red' in tmp_color:
            # print job
            last_failed_jobs.append(job)

    # print "get_job over"
    for failed_job in last_failed_jobs:
        last_build_number = server.get_job_info(failed_job)['lastBuild']['number']
        if last_build_number < LAST_BUILD_TIMES:
            iterate_counter = last_build_number
        else:
            iterate_counter = LAST_BUILD_TIMES

        tmp_job_status_list = []

        for i in range(iterate_counter-1, -1, -1):
            tmp_build_status_dict = {}
            # print last_build_number - i
            try:
                tmp_res = server.get_build_info(failed_job, last_build_number - i)['result']
            except Exception:
                continue
            tmp_key = "build{0}".format(last_build_number - i)
            if u'SUCCESS' == tmp_res:
                tmp_value = "0"
            else:
                tmp_value = "1"
            tmp_build_status_dict[tmp_key] = tmp_value
            tmp_job_status_list.append(tmp_build_status_dict)
        job_dict[failed_job] = tmp_job_status_list

    return job_dict


def init_jenkins():
    server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
    # print server
    return server


if __name__ == '__main__':
    # 实例化jenkins对象，连接远程的jenkins master server
    #server = init_jenkins()
    # server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
    # get_failed_dateset(server)
    #pass

    server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))

    # plugins = server.get_plugins_info()
    # print plugins

    print server.get_job_info(job_name[0])
    print server.get_job_info(job_name[4])['lastBuild']
    # print server.get_job_info(job_name[4])['color']
    # print server.get_job_info(job_name[0])['lastBuild']['number']

    #print server.get_build_info(job_name[1], 280)['result']
