# coding=utf-8
# author: Pan Pan
# 远程控制库

import paramiko


class RemoteCommand(object):
    # _root_pwd = "Yunshang2014"
    # _admin_pwd = "yzhxc9!"
    _root_pwd = "root"
    _admin_pwd = "admin"
    _ssh_port = 22

    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.remote_ips = []

    def set_remote_ips(self, ips):
        self.remote_ips.extend(ips)

    def clean_remote_ips(self):
        del self.remote_ips[:]

    def exec_command(self, execommand, user):
        """
        在远程机器上执行命令并且返回结果
        :param execommand:
        :param user:
        :return:
        """
        if len(self.remote_ips) == 0:
            return None
        results = {}
        for remote_ip in self.remote_ips:
            if user == "root":
                pwd = RemoteCommand._root_pwd
            elif user == "admin":
                pwd = RemoteCommand._admin_pwd
            else:
                return None
            self.ssh.connect(remote_ip, RemoteCommand._ssh_port, user, pwd)
            _, stdout, stderr = self.ssh.exec_command(execommand)
            results[remote_ip] = ("".join(stdout.readlines()), "".join(stderr.readlines()))
            self.ssh.close()
        return results

    def copy_from_remote(self, remote_file_full_path, local_file_full_path, user):
        """
        从远程机器复制文件到本地
        :param remote_file_full_path:
        :param local_file_full_path:
        :param user:
        :return:
        """
        self._copy_remote(remote_file_full_path, local_file_full_path, user, True)

    def copy_to_remote(self, remote_file_full_path, local_file_full_path, user):
        """
        将文件从本地复制到远程机器
        :param remote_file_full_path:
        :param local_file_full_path:
        :param user:
        :return:
        """
        self._copy_remote(remote_file_full_path, local_file_full_path, user, False)

    def _copy_remote(self, remote_file_full_path, local_file_full_path, user, is_from):
        """
        本地和远程机器之间复制文件
        :param remote_file_full_path:
        :param local_file_full_path:
        :param user:
        :param is_from:
        :return:
        """
        for ip in self.remote_ips:
            t = paramiko.Transport(ip, 22)
            if user == "root":
                pwd = RemoteCommand._root_pwd
            elif user == "admin":
                pwd = RemoteCommand._admin_pwd
            t.connect(username=user, password=pwd)
            sftp = paramiko.SFTPClient.from_transport(t)
            if is_from:
                sftp.get(remote_file_full_path, local_file_full_path)
            else:
                sftp.put(local_file_full_path, remote_file_full_path)
            sftp.close()
            t.close()
