# coding=utf-8
"""
TCP server
__author__ = 'zengyuetian'

"""

import socket   # socket模块


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 定义socket类型，网络通信，TCP
    s.bind((HOST, PORT))    # 套接字绑定的IP与端口
    s.listen(1)             # 开始TCP监听
    i = 0
    while 1:
        print "--------------------------------"
        conn, addr = s.accept()     # 接受TCP连接，并返回新的套接字与IP地址
        print 'Connected by', addr    # 输出客户端的IP地址
        try:
            while 1:
                data = conn.recv(1024*10)    # 把接收的数据实例化
                i += 1
        except:
            print "close connection"
            conn.close()