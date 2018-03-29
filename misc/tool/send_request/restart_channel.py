# coding=utf-8
"""
just for live testing
every night restart channel to workarround
1. delete existing channel
2. wait for minutes
3. create new channel
4. start new channel

__author__ = 'zengyuetian'

USAGE: python restart_channel.py >> restart_channel.log
INTERFACE doc: http://10.3.0.10/boss/boss/wikis/channel-srv-ix#get-live-channel-tenant_name

"""
import time
import requests
import json

# live channel server information
CHANNEL_SERVER_IP = "10.190.0.4"
CHANNEL_SERVER_PORT = 9539
TENANT = "wasu"

def GetTimeSecString():
    """
    获得当前时间戳字符串
    :return:字符串
    """
    current = time.localtime()
    time_str = time.strftime("%Y%m%d%H%M%S", current)
    return time_str


def delete_channel(channel_id, tenant_name):
    url = "/live/channel/{0}?tenant_name={1}".format(channel_id, tenant_name)
    full_url = "http://{0}:{1}{2}".format(CHANNEL_SERVER_IP, CHANNEL_SERVER_PORT, url)
    headers = {
        'accept': 'application/json'
    }
    r = requests.delete(full_url, headers=headers)
    print r.text


def create_channel(channel_name,
                   channel_source="live.hkstv.hk.lxdns.com",
                   channel_source_port="1935",
                   stream_name="/live/hks",
                   tenant_name="wasu",
                   stream_rate=500,
                   channel_capability="1000",
                   channel_factor=0.5,
                   flash_slice=3,
                   flash_delay=3,
                   flash_interval=3):
    url = "/live/channel"
    full_url = "http://{0}:{1}{2}".format(CHANNEL_SERVER_IP, CHANNEL_SERVER_PORT, url)

    headers = {
        'content-type': 'application/json',
        'accept': 'application/json'
        }

    body = {
        "channel_name": channel_name,
        "channel_source": channel_source,
        "channel_source_port": channel_source_port,
        "stream_name": stream_name,
        "tenant_name": tenant_name,
        "stream_rate": stream_rate,
        "channel_capability": channel_capability,
        "channel_factor": channel_factor,
        "flash_slice": flash_slice,
        "flash_delay": flash_delay,
        "flash_interval": flash_interval
    }

    r = requests.post(full_url, data=json.dumps(body), headers=headers)
    print r.text


def start_channel(channel_id, tenant_name):
    url = "/live/channel/{0}/start?tenant_name={1}".format(channel_id, tenant_name)
    full_url = "http://{0}:{1}{2}".format(CHANNEL_SERVER_IP, CHANNEL_SERVER_PORT, url)
    headers = {
        'accept': 'application/json'
    }
    r = requests.get(full_url, headers=headers)
    print r.text



def get_channel_ids(tenant_name):
    '''
    get all channels
    :param tenant_name:
    :return:
    '''
    url = "/live/channel?tenant_name={0}".format(tenant_name)
    full_url = "http://{0}:{1}{2}".format(CHANNEL_SERVER_IP, CHANNEL_SERVER_PORT, url)
    headers = {
        'accept': 'application/json'
    }
    r = requests.get(full_url, headers=headers)
    print r.text
    channel_ids = []
    for channel in json.loads(r.text):
        channel_ids.append(str(channel["channel_cid"]))
    return channel_ids


def test():
    channel_ids = get_channel_ids("wasu")
    print channel_ids
    for cid in channel_ids:
        delete_channel(cid, "wasu")
    time.sleep(30)
    current_time = GetTimeSecString()
    channel_name = "Test_{0}".format(current_time)
    create_channel(channel_name)
    channel_ids = get_channel_ids("wasu")
    cid = channel_ids[0]
    start_channel(cid, "wasu")


if __name__ == "__main__":
    print "===========  start  ================="

    # get the channel_id which need to be deleted
    channel_ids = get_channel_ids(TENANT)

    for cid in channel_ids:
        delete_channel(cid, TENANT)

    # sleep some time to wait delete done
    time.sleep(30)

    # create new channel
    current_time = GetTimeSecString()
    channel_name = "Test_{0}".format(current_time)
    create_channel(channel_name)

    # start channel
    channel_ids = get_channel_ids(TENANT)
    cid = channel_ids[0]
    start_channel(cid, TENANT)

    print "===========  done  ================="



