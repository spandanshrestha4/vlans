FROM python

COPY vlans.py /home/myapp

CMD python /home/myapp vlans.py


