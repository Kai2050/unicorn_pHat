#!/usr/bin/env python
#python2.7

import nmap
import time
import datetime
nm = nmap.PortScanner()


def scan():
	print("Starting scan...")
	time.sleep(1)
	nm.scan(arguments= '-sn 10.0.0.8')
	for host in nm.all_hosts():
        	print('Host : %s (%s) ' % (host, nm[host].hostname()) + ( datetime.datetime.now().strftime("%H:%M:%S")))
	time.sleep(1)
	print("Ending scan...")
	time.sleep(10)
for i in range(5):
	scan()
	time.sleep(30)
