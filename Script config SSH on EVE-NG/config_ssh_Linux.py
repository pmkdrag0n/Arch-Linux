from multiprocessing import Process
from datetime import datetime
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
import getpass
import sys
import time
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def parse(data_p):
    output_parse=parse_output(platform="cisco_ios", command="show ip int br", data=data_p)
    device_IP=output_parse[0]
    ip=device_IP["ipaddr"]
    return ip
def ansible_file():
    f=open("hosts","w")
    f.write("[all:vars]\n")
    f.write("ansible_user=admin\n")
    f.write("ansible_password="+str(master_pass)+"\n")
    f.write("ansible_connection=network_cli\n")
    f.write('ansible_become="yes"\n')
    f.write('ansible_become_method="enable"\n')
    f.write("ansible_network_os=ios\n")
    f.write("ansible_become_password=321\n")
    f.write("[device]\n")
    f.close()
def show_ip(a_device):
    list_IP=[]
    f=open("hosts","a")
    telnet = ConnectHandler(**a_device)
    output=telnet.send_command_expect("show ip int br")
    f.write(parse(output)+"\t#"+a_device["port"]+"\n")
    f.close()
    return list_IP
def config_ssh(a_device):
    telnet = ConnectHandler(**a_device)
    config_int_e0=["int e0/0",
    "no sw",
    "no shut",
    "ip add dhcp",
    ]
    config_ssh=["hostname "+a_device["port"],
    "enable pass 321",
    "username admin pass "+str(master_pass),
    "ip domain-name pmk",
    "crypto key ge rsa modul 1024",
    "line vty 0 4",
    "login local",
    "pass "+str(master_pass),
    "transport input all"
    ]
    telnet.enable()
    telnet.send_config_set(config_int_e0)
    telnet.send_config_set(config_ssh)
    telnet.disconnect()
def list_menu():
    print("#"*10+"\t IP Server EVE-NG: "+str(ip_sv)+"\t"+10*"#")
    print("")
    print("1.Cau hinh SSH cho cac thiet bi")
    print("2.Thu nhap cac IP cua thiet bi xuat ra file hosts")
    print("0.Thoat")
    print("")
    print("#"*10+"\tUsername mac dinh: admin, Enable password mac dinh: 321\t"+10*"#")
def menu():
        list_menu()
        choice=int(input("Nhap lua chon cua ban: "))
        if choice==1:
            print("Bat dau gui cau hinh len thiet bi...")
            command=config_ssh
            procs = []
            for a_device in devices:
                my_proc = Process(target=command, args=(a_device,))
                my_proc.start()
                procs.append(my_proc)
            time.sleep(10)
            print("Hoan tat cong viec")
            time.sleep(5)
            clear()
            menu()
        elif choice==2:
            print("Bat dau thu nhap IP va xuat ra file")
            command=show_ip
            ansible_file()
            procs = []
            for a_device in devices:
                my_proc = Process(target=command, args=(a_device,))
                my_proc.start()
                procs.append(my_proc)
            time.sleep(10)
            print("Hoan tat cong viec")
            time.sleep(5)
            clear()
            menu()
        elif choice==0:
            sys.exit
        else:
            print("Invalid choice selected")
if __name__ == "__main__":
    ip_sv=input("Nhap IP server EVE-NG: ")
    sl=int(input("Nhap so luong thiet bi co trong so do mang: "))
    master_pass=getpass.getpass("Nhap password SSH ban muon dat cho cac thiet bi: ")
    sw={
            "device_type" : "cisco_ios_telnet",
            "ip" : ip_sv,
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
    menu()
