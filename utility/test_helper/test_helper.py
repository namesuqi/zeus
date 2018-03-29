# coding=utf-8
"""
Tools for join Leifeng

__author__ = 'zengyuetian'

"""

from Tkinter import *
import tkMessageBox
import requests
import json
import time


def join():
    """
    function to execute for button click
    :return:
    """
    clean_log()
    if not is_peer_id_empty():
        return
    peer_id_list = get_peer_id_list()
    file_url = ch_url_var.get().strip()
    file_id = ch_fid_var.get().strip()
    print peer_id_list
    print file_url
    print file_id
    join_leifeng(file_url, file_id, peer_id_list)

def clean_log():
    log_list_text.delete(0.0, END)
    time.sleep(0.1)
    current = time.localtime()
    time_str = time.strftime("%Y/%m/%d %H:%M:%S", current)
    log(time_str)


def is_peer_id_empty():
    """
    check if peer id list is empty
    :return:
    """
    text = peer_id_list_text.get("0.0", END)
    peer_id_list = text.split()
    if len(peer_id_list) < 1:
        tkMessageBox.showinfo(title='WARN', message='Peer ID List is empty')
        return False
    else:
        return True



def get_peer_id_list():
    """
    get peer id from text list
    :return:
    """
    text = peer_id_list_text.get("0.0", END)
    peer_id_list = text.split()
    return peer_id_list


def join_leifeng(file_url, file_id, peer_id_list):
    """
    send http request to join leifeng
    :param file_url:
    :param file_id:
    :param peer_id_list:
    :return:
    """
    url = "http://stun.cloutropy.com:8000/rrpc/join_leifeng"
    log(url)

    headers = dict()
    headers["content-type"] = 'application/json'
    headers["accept"] = 'application/json'
    log(headers)

    payload = {
        "file_id": file_id,
        "file_url": file_url,
        "peer_ids": peer_id_list,
        "psize": 864,
        "ppc": 32,
        "cppc": 1,
        "push_server": "live-push.cloutropy.com"
    }
    log(payload)

    resp = requests.post(url, data=json.dumps(payload), headers =headers)
    log(resp)
    log(resp.content)

def log(content):
    log_list_text.insert(INSERT, content)
    log_list_text.insert(INSERT, "\n")


if __name__ == "__main__":
    TEXT_LENGTH = 80

    master = Tk()
    master.title("Join Leifeng Tool - by yuetian")
    var = IntVar()

    Label(master, text="Channel URL:").grid(sticky=E)
    Label(master, text="Channel FID:").grid(sticky=E)
    Label(master, text="PeerID List:").grid(sticky=E)
    Label(master, text="Log Output:").grid(sticky=E)

    ch_url_var = StringVar()
    ch_url_entry = Entry(master, textvariable=ch_url_var, width=TEXT_LENGTH)
    ch_url_var.set("http://flv.srs.cloutropy.com/wasu/test.flv")
    ch_url_entry.grid(row=0, column=1)

    ch_fid_var = StringVar()
    ch_fid_entry = Entry(master, textvariable=ch_fid_var, width=TEXT_LENGTH)
    ch_fid_var.set("23DA046BD3E2F06367C159534CE88A42")
    ch_fid_entry.grid(row=1, column=1)

    peer_id_list_text = Text(master, width=TEXT_LENGTH)
    peer_id_list_text.grid(row=2, column=1)

    log_list_text = Text(master, width=TEXT_LENGTH)
    log_list_text.grid(row=3, column=1)

    join_button = Button(master, text='Join Leifeng', command=join)
    join_button.grid(row=4, column=1)

    mainloop()