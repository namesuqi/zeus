from remote_commander import RemoteCommand
import pene_util
import time
import json
import sys
import pene_lib


if __name__ == "__main__":
    pene_lib.deploy_penetrate_sdk("10.6.4.2", "10.6.5.2")


if __name__ == "__man__":  # demo case steps
    if len(sys.argv) < 3:
        print "missing nat type parameter, script exit..."
        exit()
    Send_Nat_Type = sys.argv[1]
    Receive_Nat_Type = sys.argv[2]
    collect_folder_name = "%s_to_%s" % (Send_Nat_Type, Receive_Nat_Type)
    re = RemoteCommand()
    try:
        re.set_remote_ips(["10.6.4.1"])
        re.exec_command("nohup python /root/dummynat.py %s > /dev/null 2>&1 &" % Receive_Nat_Type, "root")
        re.clean_remote_ips()
        re.set_remote_ips(["10.6.5.1"])
        re.exec_command("nohup python /root/dummynat.py %s > /dev/null 2>&1 &" % Send_Nat_Type, "root")
        time.sleep(5)
        re.clean_remote_ips()
        re.set_remote_ips(["10.6.4.2", "10.6.5.2"])
        re.exec_command("nohup /home/admin/yssdk/ys_service_static > /dev/null 2>&1 &", "admin")
        time.sleep(2)
        if pene_util.check_peer_login(3, ["10.6.4.2", "10.6.5.2"]):
            print "SDKs login ok"
            if Receive_Nat_Type == "2":
                Receive_Nat_Type = "1"
            if Send_Nat_Type == "2":
                Send_Nat_Type = "1"
            ret_values = pene_util.get_peer_login_info(["10.6.4.2", "10.6.5.2"])
            out_str, err_str = ret_values["10.6.4.2"]
            tmp_obj = json.loads(out_str)
            if str(tmp_obj["natType"]) != Receive_Nat_Type:
                print "ip(10.6.4.2) receive nat type detective error"
            else:
                print "ip(10.6.4.2) receive nat type detective pass"
            out_str, err_str = ret_values["10.6.5.2"]
            tmp_obj2 = json.loads(out_str)
            if str(tmp_obj2["natType"]) != Send_Nat_Type:
                print "ip(10.6.5.2) send nat type detective error"
            else:
                print "ip(10.6.5.2) send nat type detective pass"
            peer_id = pene_util.get_peer_id_info("10.6.4.2")
            if peer_id:
                if pene_util.generate_ts_mock_response("3.4.0", peer_id, tmp_obj):
                    print "mock ts ok"
                    re.clean_remote_ips()
                    re.set_remote_ips(["10.6.5.2"])
                    ret_values = re.exec_command(
                        'nohup curl  --header "Range: bytes=0-335928740" -o vod.file "http://127.0.0.1:32717/vod?url='
                        'http://cdn.cloutropy.com/thunder/phone_demo_ocean_8mbps.ts&user=thunder" > /dev/null 2>&1 &',
                        "admin")
                    time.sleep(15)
                    need_rever = False
                    if Send_Nat_Type == "4":
                        need_rever = True
                    if pene_util.check_penetrator_log("10.6.5.1", True, needREVER=need_rever):
                        print "check penetrate log PASS in ip: 10.6.5.1"
                    else:
                        print "check penetrate log FAILED in ip: 10.6.5.1"
                    if pene_util.check_penetrator_log("10.6.4.1", False, needREVER=need_rever):
                        print "check penetrate log PASS in ip: 10.6.4.1"
                    else:
                        print "check penetrate log FAILED in ip: 10.6.4.1"
                else:
                    print "mock ts failed"
            else:
                print "get peer id failed, exit..."
        else:
            print "login failed, test failed, exit..."
    except:
        print "raise exception when executing test"
    finally:
        re.clean_remote_ips()
        re.set_remote_ips(["10.6.4.2", "10.6.5.2"])
        re.exec_command("ps aux | grep ys_service_static |grep -v grep |awk -F  ' ' '{print $2}' | xargs kill -9",
                        "root")
        re.clean_remote_ips()
        re.set_remote_ips(["10.6.4.1", "10.6.5.1"])
        re.exec_command("python /root/natoperator.py", "root")
    time.sleep(1)
    pene_util.collect_nat_log("10.6.4.1", collect_folder_name, "_receive")
    pene_util.collect_nat_log("10.6.5.1", collect_folder_name, "_send")
    print "test finish ..."
