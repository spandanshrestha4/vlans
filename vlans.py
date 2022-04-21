import getpass
import telnetlib

HOST = "192.168.123.100"
user = "admin"
password = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
#if password:
 #   tn.read_until(b"Password: ")
  #  tn.write(password.encode('ascii') + b"\n")

tn.write(b"en\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")


for i in range(10,50,10):
    tn.write(b"interface vlan " + str(i).encode('ascii') + b"\n")
    tn.write(b"ip address 172.16." + str(i).encode('ascii') + b".1 255.255.255.0 \n")
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





#tn.write(b"interface vlan \n")
#tn.write(b"ip address 3.3.3.3 255.255.255.255\n")

tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"exit\n")



print(tn.read_all().decode('ascii'))


