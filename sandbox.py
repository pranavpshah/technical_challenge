import numpy as np
from telnetlib import Telnet

host = "192.168.0.1"
port_num = 10100

with Telnet(host = host, port = port_num) as tn:
    tn.interact()
