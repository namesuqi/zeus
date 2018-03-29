# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""

#!/usr/bin/env python
import os
import pwd
import sys,signal


def run_cmd_with_user(command, user):
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
            os.system(command)


if __name__ == "__main__":
    command = sys.argv[1]
    user = sys.argv[2]
    run_cmd_with_user(command, user)




