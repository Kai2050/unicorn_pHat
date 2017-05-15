#!/usr/bin/env python

import nmap
import time
nm = nmap.PortScanner()


print('----------------------------------------------------')
 # If you want to do a pingsweep on network 192.168.1.0-24:

nm.scan(hosts='10.0.0.1-20', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))
