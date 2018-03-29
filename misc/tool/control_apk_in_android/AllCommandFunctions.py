#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
#         //\\        //  //=======    //=========//
#       //  \\      //  //           //         //
#     //    \\    //  //=======    //         //
#   //      \\  //  //           //         //
# //        \\//  //=========  //=========//

import os
import re
import time
import webbrowser
from jenkinsapi.jenkins import Jenkins


def get_script_dir():
    current_dir = os.getcwd()
    return current_dir


def download_new_package_from_jenkins(jenkins_url, job_name, file_path, username, password, build_url=None):
    j_server = Jenkins(jenkins_url, username, password)
    last_complete_build = j_server.get_job(job_name).get_last_completed_build().get_number()
    new_apk_build = j_server.get_job(job_name).get_last_completed_build().get_artifact_dict().items()
    apk_name = "app_%s.apk" % last_complete_build # this is use the defined apk name in jenkins
    for line in new_apk_build:
        if apk_name in line:
            new_apk_url = line[1]
            print "The newest package version ID is: %s\n" % last_complete_build
            print "Download URL is: %s\nDownloading..." % new_apk_url
            new_apk_url._do_download(file_path)
            print "Success!"


def build_packages_from_jenkins(jenkins_url, job_name, file_path, username, password):
    j_server = Jenkins(jenkins_url, username, password)
    next_build_number = j_server.get_job(job_name).get_next_build_number()
    print "Next Package Verdsion ID is: %s\nStart Pack ,please wait..." % next_build_number
    get_new_build = j_server.build_job(job_name)
    time.sleep(8*60)  # wait 8 minutes until new packages build finished
    if j_server.get_job(job_name).is_running():
        print "Need more time to pack..."
        time.sleep(3*60) # if stil in build status, then wait another 3 minutes
    last_complete_build = j_server.get_job(job_name).get_last_completed_build().get_number()
    if last_complete_build == next_build_number:
        new_apk_build = j_server.get_job(job_name).get_last_completed_build().get_artifact_dict().items()
        apk_name = "app_%s.apk" % last_complete_build  # this is use the defined apk name in jenkins
        for line in new_apk_build:
            if apk_name in line:
                new_apk_url = line[1]
                print "The new success pack ID is: %s\n" % last_complete_build
                print "Download URL is: %s\nDownloading..." % new_apk_url
                new_apk_url._do_download(file_path)
                print "Success!"
    else:
        print 'Pack Failed,please check!'
        exit()


def connect_module(script_dir, device, cmd_list):
    adb_dir = script_dir + "\\adb\\"
    for cmd in cmd_list:
        try:
            # print "Command now is: %s" %(cmd)
            os.system("%sadb -s %s %s" % (adb_dir, device, cmd))
        except OSError:
            print "[FUNCTION connect_module ERROR]: %s" % OSError


def connect_devices(script_dir, device):
    adb_dir = script_dir + "\\adb\\"
    ip_address = re.match("(.*):5555", device)
    if ip_address:
        print "Connect Device:" + ip_address.group(1)
        try:
            os.system("%sadb connect %s" % (adb_dir, ip_address.group(1)))
        except OSError:
            print "[FUNCTION connect_devices ERROR]: %s" % OSError


def adb_push_pull_cmd(cmd, f_dir, f_name=None):
    if f_name:
        rel_cmd = "%s %s %s" % (cmd, f_name, f_dir)
    else:
        rel_cmd = "%s %s" % (cmd, f_dir)
    print "[Current Command] %s" % rel_cmd
    return rel_cmd


def adb_control_pkg(cmd, package_name):
    rel_cmd = "%s %s " % (cmd, package_name)
    print "[Current Command] %s" % rel_cmd
    return rel_cmd


def clear_data_cache(files):
    relCmd = "shell rm -rf %s" % files
    print "[Current Command] %s" % relCmd
    return relCmd


def control_apk_cmd(cmd, package_name):
    relCmd = "%s %s" % (cmd, package_name)
    print "[Current Command] %s" % relCmd
    return relCmd


def get_device_ip_address(device):
    if '.' in device:
        ip = re.match("(.*):5555", device)
        return ip.group(1)
    else:
        for line in os.popen("adb -s %s shell netcfg" % device):
            ip = re.match(".*((?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]))/24", line)
            if ip:
                return ip.group(1)


def control_web_browser_cmd(url):
    webbrowser.open_new(url)
    print "[Current Command] %s" % url


def delete_local_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print "[Current Command] Delete File %s" % filename


if __name__ == '__main__':
    print "unit test"
else:
    pass
