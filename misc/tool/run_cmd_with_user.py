# coding=utf-8
"""
以其他用户启动一个daemon进程

__author__ = 'zengyuetian'

"""

#!/usr/bin/env python
import os
import pwd
import sys,signal


def run_cmd_with_user(command, user):
    os.system("echo enter {0} >> /tmp/1.txt".format(command))
    try:
        uid=pwd.getpwnam(user)
        uid=uid.pw_uid
    except:
        print "Uer not exists!"
        sys.exit(-1)

    #step two:Generation of daemon
    pid=os.fork()
    if(pid):  # father
        sys.exit(0)
    else:  # child
        os.system("echo 1 {0} >> /tmp/1.txt".format(command))
        os.setsid()
        os.chdir("/")
        os.umask(0)
        #step three :fork again
        pid=os.fork()
        if(pid==0):
            os.setuid(uid)
            os.setsid()
            os.chdir("/")
            os.umask(0)
            os.system("touch /tmp/2.txt")
            os.system(command)


if __name__ == "__main__":
    command = sys.argv[1]
    user = sys.argv[2]
    os.system("echo main {0} {1} >> /tmp/1.txt".format(command, user))
    run_cmd_with_user(command, user)




