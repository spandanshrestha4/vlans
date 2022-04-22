import os
import telnetlib
import time

#open devices file in read mode
file = open('devices.txt','r') 

for line in file:
    #read ip line by line, stripping white space
    line=line.strip()         
    
    #split ip address into array r after each .
    r=line.split('.')
    
    #take the last number of the ip address
    a=r[3]


    host = line
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
        #print("interface vlan " + str(i) )
        #print("ip address 192.168." + str(i) + "." + a )
        #print("\n")

        tn.write(b"interface vlan " + str(i).encode('ascii') + b"\n")
        tn.write(b"ip address 172.16." + str(i).encode('ascii') + b"." + a.encode('ascii') +b" 255.255.255.0 \n")
        tn.write(b"no shutdown\n")
        tn.write(b"exit\n")  


        if i==10:
            tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
            tn.write(b"name MANAGEMENT \n")
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







    



