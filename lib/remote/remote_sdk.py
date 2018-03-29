# coding=utf-8
"""
get peer info

__author__ = 'zengyuetian'

"""
import paramiko

def get_peer_info(ip_list, username, passwd, num_list, save_file):
    fp = open(save_file, "w+")
    for index, lf_ip in enumerate(ip_list):
        print "Start get peer info on {0}".format(lf_ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(lf_ip, 22, username, passwd, timeout=5)
        for i in range(num_list[index]):
            cmd = "cat /home/admin/live/{0}/yunshang/yunshang.conf".format(i)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            line = stdout.readline()
            print "IP:" + lf_ip + "; DIR: " + str(i) + "; LINE: " + line
            fp.write(line)
            fp.write("\n")
        ssh.close()
    fp.close()

if __name__ == "__main__":
    for i, j in enumerate([1, 2, 3, 4]):
        print i, j

