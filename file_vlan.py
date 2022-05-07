import telnetlib
from netmiko import ConnectHandler

devices = ["192.168.123.100",
           "192.168.123.101",
           "192.168.123.102",
           "192.168.123.103",
           "192.168.123.50" ]

for ip_address in devices:
    all_devices = {
    "device_type": "cisco_ios",
    "ip":ip_address,
    "username": "admin",
    "password": "cisco",
    "secret": "cisco@123"
    }

    net_connect = ConnectHandler(**all_devices)
    net_connect.enable()
    
    #split ip address into array after each .
    split_ip=ip_address.split('.')
    
    #take the last number of the ip address
    network_ip=split_ip[3]


   
    for i in range(10,50,10):
        config_commands1 = ["interface vlan " + str(i),
                            "ip address 172.16." + 
                            str(i)+ "." +
                            network_ip +
                            " 255.255.255.0",
                            "no shutdown",
                            "exit"]

        vlan_ip = net_connect.send_config_set(config_commands1)
        print(vlan_ip)

        
        
    config_commands2 = ["vlan 10",
                        "name Admission",
                        
                        "vlan 20",
                        "name Staff",
                        
                        "vlan 30",
                        "name Students",
                        
                        "vlan 40",
                        "name R&D" ]

    vlan_name = net_connect.send_config_set(config_commands2)
    print(vlan_name)


    save = net_connect.save_config()
    print(save)



net_connect.disconnect()