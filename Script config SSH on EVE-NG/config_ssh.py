from netmiko import Netmiko
from ntc_templates.parse import parse_output
from datetime import datetime
def config(sl,ip_sv,porttel=32769):
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
    for x in range (sl):
        telnet=Netmiko(device_type="cisco_ios_telnet",ip=ip_sv,port=porttel,secret="321",blocking_timeout=16)
        telnet.enable()
        print("Configuring Device "+str(x+1)+"...")
        telnet.send_config_set(config_int_e0)
        telnet.send_config_set(config_ssh)
        porttel=porttel+1
        telnet.disconnect()
def parse(data_out):
        output_parse=parse_output(platform="cisco_ios", command="show ip int br", data=data_out)
        device_IP=output_parse[0])

def showIp(sl,ip_sv,porttel=32769):
    list_IP=[]
    n=1
    f=open("log.txt", "w")
    for x in range (sl):
        telnet=Netmiko()
        print("Dang lay IP device "+str(n))
        porttel=porttel+1
        n=n+1
        output=telnet.send_command("show ip int br",delay_factor=0)
        parse(output)
        #
    #   device_IP=output_parse[0]
    #    list_IP.append(device_IP["ipaddr"])

        telnet.disconnect()
'''
    print("Dang xuat ra file...")

    #f.write("="*50+str(datetime.now())+"="*50+"\n")
    for x in list_IP:
        f.write(str(x)+"\n")
    f.close()
'''
if __name__ == '__main__':
    ip_sv=input("Nhap IP server EVE-NG: ")
    sl=int(input("So luong thiet bi co trong so do lab: "))
    porttel=32769
    print("1.Cau hinh SSH cho cac thiet bi")
    print("2.Thu nhap cac IP cua thiet bi")
    choice=input("Nhap lua chon cua ban: ")
    if choice=="1":
        config(sl,ip_sv)
    if choice=="2":
        showIp(sl,ip_sv)
