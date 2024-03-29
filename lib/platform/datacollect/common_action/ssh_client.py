import paramiko
import time


class SSHClient(object):

    def __init__(self, ip, username, password):
        start = time.time()
        print "SSHConnect to {0}, it should be only call one time!!!".format(ip)
        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(ip, 22, username, password)
        end = time.time()
        print "SSHConnection cost {0} seconds.".format(start - end)

    def __del__(self):
        print 'SSHConnection close!'
        self._ssh.close()

    def execute_command(self, command):
        remote_terminal_return = self._ssh.exec_command(command)
        print '------------------------------------------------------'
        for item in remote_terminal_return[1].readlines():
            print item,
        print '------------------------------------------------------'


if __name__ == '__main__':
    ssh = SSHClient('10.5.100.46', 'root', 'Yunshang2014')
    ssh.excute_command('ifconfig')
