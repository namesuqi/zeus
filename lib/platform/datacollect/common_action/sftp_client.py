import paramiko
import time


class SFTPClient(object):
    def __init__(self, ip, username, password):
        start = time.time()
        print "SFTPConnect to {0}, it should be only call one time!!!".format(ip)
        self._transport = paramiko.Transport(ip, 22)
        self._transport.connect(None, username, password)
        self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        end = time.time()
        print "SFTPConnection cost {0} seconds.".format(start - end)

    def __del__(self):
        print 'SFTPConnection close!'
        self._transport.close()

    def upload(self, remote_path, local_path):
        self._sftp.put(local_path, remote_path)
        print '---------------------'
        print '|  Upload Success!  |'
        print '---------------------'

    def download(self, remote_path, local_path):
        self._sftp.get(remote_path, local_path)
        print '---------------------'
        print '| Download Success! |'
        print '---------------------'


if __name__ == '__main__':
    sftp = SFTPClient('10.5.100.46', 'root', 'Yunshang2014')
    sftp.upload('/root/Testdata/123.test', 'd://test.txt')
    sftp.download('/root/Testdata/123.test', 'd://test123.txt')
