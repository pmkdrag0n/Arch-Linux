#import threading
from multiprocessing import Process
from datetime import datetime
from netmiko import ConnectHandler

def show_ip(a_device):
    remote_conn = ConnectHandler(**a_device)
    print()
    print("#" * 80)
    print(remote_conn.send_command_expect("show ip int br"))
    print("#" * 80)
    print()



def main():
    print("1.Cau hinh SSH cho cac thiet bi")
    print("2.Thu nhap cac IP cua thiet bi")
    choice=input("Nhap lua chon cua ban: ")
    if choice=="1":
        command=config_ssh
    if choice=="2":
        command=show_ip
    procs = []
    for a_device in devices:
        my_proc = Process(target=command, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)
if __name__ == "__main__":
    sl=int(input("Nhap sl:"))
    sw={
            "device_type" : "cisco_ios_telnet",
            "ip" : "192.168.1.129",
            "port" :"32769",
            "secret":"321"
            }
    portt=32769
    devices=[]
    for n in range (sl):
        sw1=sw.copy()
        sw1["port"]=str(portt)
        devices.append(sw1)
        portt=portt+1
    main()
