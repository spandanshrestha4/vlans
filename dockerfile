FROM python


RUN pip install netmiko

COPY file_vlan.py /home/myapp


CMD python /home/myapp file_vlan.py




