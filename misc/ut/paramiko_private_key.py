# coding=utf-8
# author: zengyuetian

# !/usr/bin/env python
import paramiko

hostname = '133.214.210.124'
port = 22
username = 'root'
pkey = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey)
s = paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname, port, username, pkey=key)
stdin, stdout, stderr = s.exec_command('hostname')

print stdout.read()
