# coding=utf-8
"""
automation test entrance base class
define basic test steps

__author__ = 'zengyuetian'

"""

from lib.constant.database import *
from lib.utility.path import *


class ExecutorBase(object):
    def prepare_environment(self):
        self.add_python_path()
        # self.print_hosts()
        # self.restore_mysql()

    def deploy_agent(self):
        pass

    def deploy_sdk(self):
        pass

    @staticmethod
    def start_robot_framework(include_type, tags):
        include_string = ""

        if include_type == "case":
            include = " --test "
        elif include_type == "suite":
            include = " --suite "
        else:
            include = " --include "

        for tag in tags:
            include_string = include_string + include + tag

        root_path = PathController.get_root_path()
        command = 'cd {0}; pybot -d result --debugfile debug.txt {1} ./testsuite'.format(root_path, include_string)
        os.system(command)

    @staticmethod
    def collect_result():
        webdir = "/var/www/html/"
        user_dir = webdir + PathController.get_root_dir_name()
        root_path = PathController.get_root_path()
        os.system("mkdir -p {0}".format(webdir))
        os.system("mkdir -p {0}".format(user_dir))
        os.system("cp -Rf {0}/result {1}".format(root_path, user_dir))

    @staticmethod
    def add_python_path():
        zeus_path = PathController.get_root_path()
        sys.path.append(zeus_path)
        print "Add PYTHON_PATH done."

    def print_hosts(self):
        # subprocess.call("cat /etc/hosts", shell=True)
        pass

    @staticmethod
    def restore_mysql():
        root_path = PathController.get_root_path()
        command = 'mysql -h{0} -u{1} -p{2} -e "use boss; source {3}/misc/sql/test_boss.sql;"'.\
            format(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, root_path)
        print command
        os.system(command)


if __name__ == "__main__":
    ExecutorBase().print_hosts()


