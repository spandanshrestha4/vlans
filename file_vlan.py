import telnetlib
import time

 
devices = ['192.168.123.100','192.168.123.102','192.168.123.103']

for ip_address in devices:
    
    #split ip address into array after each .
    split_ip=ip_address.split('.')
    
    #take the last number of the ip address
    a=split_ip[3]


    host = ip_address
    user = "admin"
    password = "cisco"
    tn = telnetlib.Telnet(host)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    tn.write(b"en\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")

    
    for i in range(10,50,10):
        tn.write(b"interface vlan " + str(i).encode('ascii') + b"\n")
        tn.write(b"ip address 172.16." + str(i).encode('ascii') + b"." + a.encode('ascii') +b" 255.255.255.0 \n")
        tn.write(b"no shutdown\n")
        tn.write(b"exit\n")  


        if i==10:
            tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
            tn.write(b"name ADMISSION_TEAM \n")
        if i==20:
            tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
            tn.write(b"name STAFF \n")
        if i==30:
            tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
            tn.write(b"name STUDENTS \n")

        if i==40:
            tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
            tn.write(b"name RESEARCH \n")    


    tn.write(b"exit\n")
    tn.write(b"exit\n")
    tn.write(b"copy r st\n")
    time.sleep(.5)
    tn.write(b"\n")
    tn.write(b"exit\n")



    print(tn.read_all().decode('ascii'))







    



