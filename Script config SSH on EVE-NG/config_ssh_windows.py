from netmiko import ConnectHandler
from multiprocessing import Process
import time
def config_ssh(a_device):
        config_int_e0=["int e0/0",
        "no sw",
        "no shut",
        "ip add dhcp"
        ]
        config_ssh=[
        "enable pass 321",
        "username admin pass 123",
        "ip domain-name pmk",
        "crypto key ge rsa modul 1024",
        "line vty 0 15",
        "login local",
        "pass 123"
        ]
        telnet = ConnectHandler(**a_device)
        telnet.enable()
        telnet.send_config_set(config_int_e0)
        telnet.send_config_set(config_ssh)
        telnet.disconnect()
def show_ip(a_device):
        telnet=ConnectHandler(**a_device)
        print("*"*80)
        print(telnet.send_command_expect("show ip int br"))
        print("*"*80)
def list_menu():
    print("1.Cau hinh SSH cho cac thiet bi")
    print("2.Show ip interface brief")
    print("0.Thoat")
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
        menu()
    elif choice==2:
        print("Bat dau thi nhap IP va xuat ra file")
        command=show_ip
        procs = []
        for a_device in devices:
            my_proc = Process(target=command, args=(a_device,))
            my_proc.start()
            procs.append(my_proc)
        time.sleep(10)
        print("Hoan tat cong viec")
        menu()
    elif choice==0:
        sys.exit
    else:
        print("Invalid choice selected")

if __name__ == '__main__':
    ip_sv=input("Nhap IP server EVE-NG: ")
    sl=int(input("Nhap so luong thiet bi co trong so do mang: "))
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
