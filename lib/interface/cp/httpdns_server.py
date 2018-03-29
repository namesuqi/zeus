# coding=utf-8

"""

httpdns相关服务器访问接口
__author__ = 'liwenxuan'

"""
import hashlib
import time
from lib.constant.request import *
from lib.constant.various import PROVINCE_IP_LIST
from lib.request.header_data import *
from lib.request.http_request import *
from lib.decorator.trace import *


@print_trace
def ip_into_int(ip):
    """
    将IP转化为整数
    :param ip:
    :return:
    """
    ip_int = reduce(lambda x, y: (x << 8)+y, map(int, ip.split('.')))
    return int(ip_int)


@print_trace
def httpdns_get_host(protocol, host, port, param_host, src_ip=None, ip_para=False, ip_header=True):
    """
    请求指定域名对应的IP
    :param protocol:
    :param host:
    :param port:
    :param param_host:
    :param src_ip:
    :param ip_para: URI中是否携带IP参数
    :param ip_header: 请求header中是否携带X-Real-IP（负载均衡转发时header所带源IP）
    :return:
    """
    url = "/httpdns/host?host=" + str(param_host)
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if src_ip is not None and ip_para:
        url = "/httpdns/host?host=" + str(param_host) + "&ip=" + str(src_ip)

    if src_ip is not None and ip_header:
        headers = HeaderData().Content__Type('application/json').X__Real__IP(src_ip)\
            .ACCEPT('application/json').get_res()

    response = send_request(
        '[HttpdnsGetHost]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def httpdns_get_hosts(protocol, host, port, param_group, src_ip=None, ip_para=False, ip_header=True):
    """
    请求指定域名组对应的IP
    :param protocol:
    :param host:
    :param port:
    :param param_group:
    :param src_ip:
    :param ip_para: URI中是否携带IP参数
    :param ip_header: 请求header中是否携带X-Real-IP（负载均衡转发时header所带源IP）
    :return:
    """

    url = "/httpdns/hosts?groupName=" + str(param_group)
    headers = HeaderData().Content__Type('application/json').ACCEPT('application/json').get_res()

    if src_ip is not None and ip_para:
        url = "/httpdns/hosts?groupName=" + str(param_group) + "&ip=" + str(src_ip)

    if src_ip is not None and ip_header:
        headers = HeaderData().Content__Type('application/json').X__Real__IP(src_ip)\
            .ACCEPT('application/json').get_res()

    response = send_request(
        '[HttpdnsGetHost]',
        protocol,
        GET,
        host,
        port,
        url,
        headers,
        None,
        None
    )
    return response


@print_trace
def check_httpdns_host_res(httpdns_host, httpdns_port, provinces, domains, expect_ip, ips_len, expect_ttl=None,
                           only=False):
    """
    检查httpdns-srv能否根据源IP返回对应域名信息
    :param provinces: province list
    :param domains: domain list
    :param expect_ip: 期望返回的IP的开头两段地址（与配置相对应）, eg:"1.1"
    :param ips_len: Etcd配置中域名对应IP列表元素个数
    :param expect_ttl: 期望返回的TTL值, 为None则不检查
    :param only: 少量请求
    :return:
    """

    for k, v in PROVINCE_IP_LIST.iteritems():
        if k in provinces:
            if only and hashlib.md5(k).hexdigest()[-1] > '4':
                pass
            else:
                print "PROVINCE ID:", k
                for ip in v:
                    print "|||=========================Src ip: %s =========================|||" % str(ip)
                    ips_index = ip_into_int(ip) % int(ips_len)  # 请求源IP映射到域名IP列表中对应元素索引
                    for domain in domains:
                        for i in range(2):
                            if i == 0:
                                # 请求header中携带X-Real-IP参数，URI中不携带IP参数
                                res = httpdns_get_host(HTTP, httpdns_host, httpdns_port, domain, ip, ip_para=False,
                                                       ip_header=True).json()
                            elif i == 1:
                                # 请求URI中携带IP参数，header中不携带
                                res = httpdns_get_host(HTTP, httpdns_host, httpdns_port, domain, ip, ip_para=True,
                                                       ip_header=False).json()

                            time.sleep(0.005)
                            domain_ips = res["ips"]
                            if len(domain_ips) != 1:  # 返回域名IP列表中应只有一个IP（需求设计）
                                print "Should be only one".ljust(120, "*")
                                print "Real domain ips:", domain_ips
                                return False
                            domain_ip = domain_ips[0]
                            domain_ip_split = domain_ip.split(".")
                            if domain_ip_split[:2] != expect_ip.split("."):  # 比较域名IP前两段是否与特征值相符
                                print "Domain IP should start with %s" % (str(expect_ip)).ljust(120, "*")
                                print "Real domain ips:", domain_ips
                                return False
                            if domain_ip_split[-1] != str(ips_index):  # 配置中域名IP最后一段数值表示该IP在列表中的索引
                                print "Domain IP should end with %s" % (str(ips_index)).ljust(120, "*")
                                print "Real domain ips:", domain_ips
                                return False
                            if expect_ttl is not None:  # 是否检查ttl
                                if res["ttl"] != int(expect_ttl):
                                    print "Domain TTL should be %s" % (str(expect_ttl)).ljust(120, "*")
                                    print "Real domain ttl:", res["ttl"]
                                    return False
    return True


@print_trace
def check_httpdns_group_res(httpdns_host, httpdns_port, provinces, domain_group, domains, expect_ip, ips_len,
                            expect_ttl=None, only=False):
    """
    检查httpdns-srv能否根据源IP返回对应域名组信息
    :param httpdns_host:
    :param httpdns_port:
    :param provinces:
    :param domain_group: 需要获取的域名组，eg: cloutropy.com
    :param domains: 需要检查的域名列表，不在该列表内的域名不检查，eg: ["ts.cloutropy.com", "report,cloutropy.com"]
    :param expect_ip:
    :param ips_len:
    :param expect_ttl:
    :param only:
    :return:
    """
    for k, v in PROVINCE_IP_LIST.iteritems():
        if k in provinces:
            if only and hashlib.md5(k).hexdigest()[-1] > '4':
                pass
            else:
                print "PROVINCE ID:", k
                for ip in v:
                    print "|||=========================Src ip: %s=========================|||" % str(ip)
                    ips_index = ip_into_int(ip) % int(ips_len)  # 请求源IP映射到域名IP列表中对应元素
                    for i in range(2):
                        if i == 0:
                            res = httpdns_get_hosts(HTTP, httpdns_host, httpdns_port, domain_group, ip, ip_para=False,
                                                    ip_header=True).json()
                        elif i == 1:
                            res = httpdns_get_hosts(HTTP, httpdns_host, httpdns_port, domain_group, ip, ip_para=True,
                                                    ip_header=False).json()
                        time.sleep(0.005)
                        as_len = 0  # 返回域名列表中指定域名元素个数
                        for domain_info in res:
                            if domain_info["host"] in domains:  # 返回域名列表中指定域名信息
                                as_len += 1
                                domain_ips = domain_info["ips"]
                                domain_ttl = domain_info["ttl"]
                                if len(domain_ips) != 1:
                                    print "Should be only one".ljust(120, "*")
                                    print "Should be only one".ljust(120, "*")
                                    print "Real domain ips:", domain_ips
                                    return False
                                domain_ip = domain_ips[0]
                                domain_ip_split = domain_ip.split(".")
                                if domain_ip_split[:2] != expect_ip.split("."):
                                    print "Domain IP should start with %s" % (str(expect_ip)).ljust(120, "*")
                                    print "Real domain ips:", domain_ips
                                    return False
                                if domain_ip_split[-1] != str(ips_index):
                                    print "Domain IP should end with %s" % (str(ips_index)).ljust(120, "*")
                                    print "Real domain ips:", domain_ips
                                    return False
                                if expect_ttl is not None:
                                    if domain_ttl != int(expect_ttl):
                                        print "Domain TTL should be %s" % (str(expect_ttl)).ljust(120, "*")
                                        print "Real domain ttl:", res["ttl"]
                                        return False
                        if as_len != len(domains):  # 判断返回中指定域名元素是否有缺失或重复
                            print "Domain count error.".ljust(120, "*")
                            print "Actual num: %s, expect num: %s" % (str(as_len), str(len(domains)))
                            print "Check domains(should exist): %s" % (str(domains))
                            print "Real domains:",
                            for x in res: print x["host"], ",",
                            return False

    return True


if __name__ == "__main__":
        HTTPDNS_IP = "192.168.4.249"
        # r1 = check_httpdns_host_res(DEFAULT_PROVINCE, GROUP_DOMAINS_CLOUTROPY, "0.0", 5, 3600)
        # r2 = check_httpdns_host_res(NORTH_PROVINCE, PART_DOMAIN_CLOUTROPY, "1.1", 4, 1000)
        # r3 = check_httpdns_host_res(SOUTH_PROVINCE, PART_DOMAIN_CLOUTROPY, "2.2", 6, 2000)
        # r4 = check_httpdns_host_res(GUANGXI_PROVINCE, PART_DOMAIN_CLOUTROPY, "3.3", 2, 3000)
        # r5 = check_httpdns_host_res(PROVINCE_LIST, DEFAULT_DOMAIN_CLOUTROPY, "0.0", 5, 3600)
        # print r1, r2, r3, r4, r5
        # httpdns_get_hosts("HTTP", HTTPDNS_IP, 9500, "cloutropy.com", ).json()
        # s1 = check_httpdns_group_res(HTTPDNS_IP, 9500, DEFAULT_PROVINCE, GROUP_CLOUTROPY, GROUP_DOMAINS_CLOUTROPY, "0.0", 5, 3600)
        # s2 = check_httpdns_group_res(HTTPDNS_IP, 9500, NORTH_PROVINCE, GROUP_CLOUTROPY, PART_DOMAIN_CLOUTROPY, "1.1", 4, 1000)
        # s3 = check_httpdns_group_res(HTTPDNS_IP, 9500, SOUTH_PROVINCE, GROUP_CLOUTROPY, PART_DOMAIN_CLOUTROPY, "2.2", 6, 2000)
        # s4 = check_httpdns_group_res(HTTPDNS_IP, 9500, GUANGXI_PROVINCE, GROUP_CLOUTROPY, PART_DOMAIN_CLOUTROPY, "3.3", 2, 3000)
        # s5 = check_httpdns_group_res(HTTPDNS_IP, 9500, PROVINCE_LIST, GROUP_CLOUTROPY, DEFAULT_DOMAIN_CLOUTROPY, "0.0", 5, 3600)
        # print s1, s2, s3, s4, s5

        # httpdns_host = "httpdns.cloutropy.com"
        # httpdns_port = "80"
        # for k, v in PROVINCE_IP_LIST.iteritems():
        #     print "PROVINCE ID:", k
        #     ip = v[0]
        #     res = httpdns_get_hosts(HTTP, httpdns_host, httpdns_port, GROUP_CLOUTROPY, ip, ip_para=True, ip_header=False).json()
        #     for domain in GROUP_DOMAINS_CLOUTROPY:
        #         res = httpdns_get_host(HTTP, httpdns_host, httpdns_port, domain, ip, ip_para=True, ip_header=False).json()
