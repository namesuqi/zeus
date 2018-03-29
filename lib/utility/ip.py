# coding=utf-8
"""
create ip list

__author__ = 'zengyuetian'

"""

def create_private_ip_list(num=1000):
    ips = []
    total = 0
    for i in range(1, 255):
        for j in range(1, 255):
            ips.append("192.168.{0}.{1}".format(i, j))
            total += 1
            if total >= num:
                break
        if total >= num:
            break

    return ips


if __name__ == "__main__":
    ips = create_private_ip_list()
    for ip in ips:
        print ip

