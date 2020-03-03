from netmiko import ConnectHandler
ip_sv=input("Nhap IP server EVE-NG: ")
n=int(input("So luong thiet bi: "))
porttn=32769
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
"line vty 0 4",
"login local",
"pass 123"
]
for x in range (n):
    telnet= ConnectHandler(device_type="cisco_ios_telnet",ip=ip_sv,port=porttn,secret="321",blocking_timeout=16)
    telnet.enable()
    print("Configuring device "+ str(x)+"...")
    telnet.send_config_set(config_int_e0)
    telnet.send_config_set(config_ssh)
    output = telnet.send_command("show ip int brief",delay_factor=12)
    print(output)
    print("#"*50)
    porttn=porttn+1
    telnet.disconnect()
