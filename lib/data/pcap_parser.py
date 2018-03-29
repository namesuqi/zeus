# coding=utf-8
"""
pcap file parser

precondition: pip install dpkt

__author__ = 'zengyuetian'

"""

import dpkt
import socket
import datetime


class PcapParser(object):
    # !/usr/bin/env python
    """
    Use DPKT to read in a pcap file and print out the contents of the packets
    This example is focused on the fields in the Ethernet Frame and IP packet
    """

    def mac_addr(self, address):
        """Convert a MAC address to a readable/printable string

           Args:
               address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
           Returns:
               str: Printable/readable MAC address
        """
        return ':'.join('%02x' % ord(b) for b in address)



    def ip_to_str(self, address):
        """Print out an IP address given a string

        Args:
            address (inet struct): inet network address
        Returns:
            str: Printable/readable IP address
        """
        return socket.inet_ntop(socket.AF_INET, address)



    def print_packets (self, pcap):
        """Print out information about each packet in a pcap

           Args:
               pcap: dpkt pcap reader object (dpkt.pcap.Reader)
        """
        # For each packet in the pcap process the contents
        for timestamp, buf in pcap:

            # Print out the timestamp in UTC
            print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))

            # Unpack the Ethernet frame (mac src/dst, ethertype)
            eth = dpkt.ethernet.Ethernet(buf)
            print 'Ethernet Frame: ', self.mac_addr(eth.src), self.mac_addr(eth.dst), eth.type

            # Make sure the Ethernet frame contains an IP packet
            # EtherType (IP, ARP, PPPoE, IP6... see http://en.wikipedia.org/wiki/EtherType)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
                continue

            # Now unpack the data within the Ethernet frame (the IP packet)
            # Pulling out src, dst, length, fragment info, TTL, and Protocol
            ip = eth.data

            # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
            do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

            ip_data = ip.data
            # if ip_data.dport == 80 and len(ip_data.data) > 0:
            #     http = dpkt.http.Request(ip_data.data)
            #     print "http body", http.body
            #     print "http uri", http.uri
            #     print "http method", http.method
            #     print "http headers", http.headers
            #     print "http version", http.version
            #
            # if (ip_data.dport == 9000 or ip_data.dport == 9002) and len(ip_data.data) > 0:
            #     print "Got it."
            #     # try:
            #     #     udp = dpkt.udp.UDP(tcp.data)
            #     # except dpkt.dpkt.NeedData:
            #     #     pass
            #     # except dpkt.dpkt.UnpackError:
            #     #     pass
            #     # else:
            #     print "udp data", ip_data.data
            #     print "udp data size", len(ip_data.data)

            if isinstance(ip_data, dpkt.udp.UDP):
                udp = ip_data
                if udp.dport == 9000 or udp.dport == 9002:
                    stun = dpkt.stun.STUN(udp)
                    print stun.data
                    print stun.len
                    print stun.type
                    print stun.xid



            # Print out the info
            print 'IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' % \
                  (self.ip_to_str(ip.src), self.ip_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments,
                   fragment_offset)

    def test(self):
        """Open up a test pcap file and print out the packets"""
        with open('/root/26.pcap', 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
            self.print_packets(pcap)

if __name__ == '__main__':
    PcapParser().test()



