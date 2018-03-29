#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
#         //\\        //  //=======    //=========//
#       //  \\      //  //           //         //
#     //    \\    //  //=======    //         //
#   //      \\  //  //           //         //
# //        \\//  //=========  //=========//

# 请将脚本放置在英文目录下
# 常量数据配置在 easydata.py文件中配置
# 调用方法在 AllCommandFunctions.py 文件中
# 使用jenkins打包需要登录git vpn，否则将失败

from AllCommandFunctions import *

# import data configuration, defined by each device and environments
# Include jenkins related data , demo apk data info and android devices info
from easydata import *


def rel_operation_on_android(choice_number):
    exec_cmd_list = []
    if choice_number == "0":
        control_web_browser_cmd(build_url)  # OPEN JENKINS BUILD WEB
        delete_local_file(apk_dir)  # DELETE LOCAL APK FILE
        build_packages_from_jenkins(JENKINS_URL, JOB_NAME, apk_dir, JENKINS_USER, JENKINS_PASSWORD)  # BUILD NEW VERSION
    elif choice_number == "1":
        exec_cmd_list.append(adb_control_pkg("install", apk_dir))  # INSTALL APK
        exec_cmd_list.append(control_apk_cmd("shell am start -n", "%s/%s" % (PKG_NAME, pkg_activity)))  # START INSTALL
    elif choice_number == "2":
        exec_cmd_list.append(adb_control_pkg("uninstall", PKG_NAME))  # UNINSTALL INSTALL
        exec_cmd_list.append(adb_control_pkg("install", apk_dir))  # INSTALL
        exec_cmd_list.append(control_apk_cmd("shell am start -n", "%s/%s" % (PKG_NAME, pkg_activity)))  # START INSTALL
    elif choice_number == "3":
        exec_cmd_list.append(control_apk_cmd("shell am force-stop", "%s/%s" % (PKG_NAME, pkg_activity)))  # STOP INSTALL
        exec_cmd_list.append(control_apk_cmd("shell am start -n", "%s/%s" % (PKG_NAME, pkg_activity)))  # START INSTALL
    elif choice_number == "4":
        exec_cmd_list.append(adb_control_pkg("uninstall", PKG_NAME))
    elif choice_number == "5":
        exec_cmd_list.append(clear_data_cache(file_data))  # DELETE FILE
        exec_cmd_list.append(clear_data_cache(file_meta))  # DELETE FILE
    elif choice_number == "6":
        # exec_cmd_list.append(control_apk_cmd("root"))
        # exec_cmd_list.append(control_apk_cmd("mount -o rw,remount /dev/block/system /system")) # reload system disk to mode rw
        exec_cmd_list.append(adb_push_pull_cmd("push", "/sdcard/yunshang", "hostfiles/testupgradehosts"))  # UPLOAD FILE TO ANDROID
    elif choice_number == "7":
        exec_cmd_list.append(adb_push_pull_cmd("pull", "/sdcard/yunshang/yunshang.conf"))  # DOWNLOAD FILE FROM

    elif choice_number == "r" or "R":
        pass
        # exec_cmd_list.append("shell reboot")
    elif choice_number == "q" or "Q":
        exit()
    else:
        print "[SORRY ERROR CHOICE]:" + choice_number

    connect_module(script_dir, ANDROID_DEVICE, exec_cmd_list)
    rel_operation_on_android(welcome())


def welcome():
    print " ********Command List********"
    print "[0]: Build new apk in Jenkins"
    print "[1]: Install apk-------------"
    print "[2]: Re-install apk----------"
    # print "[3]: Restart apk-------------"
    print "[4]: Un-install apk----------"
    print "[5]: Delete data file--------"
    print "*****************************"
    print "[6]: Up file to Android------"
    print "[7]: Get file from Android---"
    print "[R]: Restart Android Device--"
    print "[Q]: Quit--------------------"
    cmd_number = raw_input("[Enter Command]: ")
    return cmd_number

if __name__ == '__main__':
    script_dir = get_script_dir()

    # ANDROID_DEVICE = "192.168.1.65:5555"
    # ANDROID_DEVICE = "248291524419" #XIAO MI
    ANDROID_DEVICE = "6NJUMLZL0J" #KAI BO ER H19
    # ANDROID_DEVICE = "0123456789ABCDEF" # HW M310

    device_ip = get_device_ip_address(ANDROID_DEVICE)

    apk_dir = "apkpackages/%s" % APK_NAME
    pkg_activity = "%s.%s" % (PKG_NAME, ACTIVITY)

    file_data = "%s/yunshang.data" % FILE_DIR
    file_meta = "%s/yunshang.meta" % FILE_DIR
    version_url = "http://%s:32719/ajax/version" % device_ip
    index_url = "http://%s:32719/dashboard/index" % device_ip

    build_url = "%s/job/%s" % (JENKINS_URL, JOB_NAME)

    connect_devices(script_dir, ANDROID_DEVICE)
    rel_operation_on_android(welcome())
else:
    pass
