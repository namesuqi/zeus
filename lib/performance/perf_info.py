# coding=utf-8
"""
get machine's performance information

__author__ = 'zengyuetian'

"""
import time
import os
import psutil

def get_memory_used():
    '''
    get memory size in use(M)
    '''
    mem = psutil.virtual_memory()
    return mem.used/(1024*1024)

def get_memory_percent():
    '''
    get memory percentage in use
    '''
    mem = psutil.virtual_memory()
    return mem.percent

def get_cpu_idle_percent():
    '''
    get idle cpu percentage
    '''
    cpu_time_percent = psutil.cpu_times_percent()
    return cpu_time_percent.idle

def byte_to_human(n):
    """
    n = 10000
    '9.8 K'
    n = 100001221
    '95.4 M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f %s' %(value, s)
    return '%.2f B' %(n)


def net_poll(interval):
    """Retrieve raw stats within an interval window."""
    tot_before = psutil.net_io_counters()
    pnic_before = psutil.net_io_counters(pernic=True)
    # sleep some time
    time.sleep(interval)
    tot_after = psutil.net_io_counters()
    pnic_after = psutil.net_io_counters(pernic=True)
    return (tot_before, tot_after, pnic_before, pnic_after)


def refresh_window(tot_before, tot_after, pnic_before, pnic_after):
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    """Print stats on screen."""

    # totals
    print(" NetStates:")
    # print("total bytes:                     sent: %-10s     received: %s" % (byte_to_human(tot_after.bytes_sent),
    #                                                                          byte_to_human(tot_after.bytes_recv))
    #       )
    # print("total packets:                 sent: %-10s     received: %s" % (tot_after.packets_sent,
    #                                                                        tot_after.packets_recv)
    #       )
    # per-network interface details: let's sort network interfaces so
    # that the ones which generated more traffic are shown first
    print("")
    nic_names = pnic_after.keys()
    # nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)
    templ = "%-15s %15s %15s"
    print(templ % ("TOTAL", "PER-SEC", ""))

    print(templ % (
        "bytes-sent",
        byte_to_human(tot_after.bytes_sent),
        byte_to_human(tot_after.bytes_sent - tot_before.bytes_sent) + '/s',
    ))

    print(templ % (
        "bytes-recv",
        byte_to_human(tot_after.bytes_recv),
        byte_to_human(tot_after.bytes_recv - tot_before.bytes_recv) + '/s',
    ))

    # for name in nic_names:
    #     stats_before = pnic_before[name]
    #     stats_after = pnic_after[name]
    #     templ = "%-15s %15s %15s"
    #     print(templ % (name, "TOTAL", "PER-SEC"))
    #     print(templ % (
    #         "bytes-sent",
    #         byte_to_human(stats_after.bytes_sent),
    #         byte_to_human(stats_after.bytes_sent - stats_before.bytes_sent) + '/s',
    #     ))
    #     print(templ % (
    #         "bytes-recv",
    #         byte_to_human(stats_after.bytes_recv),
    #         byte_to_human(stats_after.bytes_recv - stats_before.bytes_recv) + '/s',
    #     ))
    #     print(templ % (
    #         "pkts-sent",
    #         stats_after.packets_sent,
    #         stats_after.packets_sent - stats_before.packets_sent,
    #     ))
    #     print(templ % (
    #         "pkts-recv",
    #         stats_after.packets_recv,
    #         stats_after.packets_recv - stats_before.packets_recv,
    #     ))
    #     print("")

if __name__ == "__main__":
    try:
        interval = 0
        while 1:
            args = net_poll(interval)
            refresh_window(*args)
            interval = 1
    except (KeyboardInterrupt, SystemExit):
        pass