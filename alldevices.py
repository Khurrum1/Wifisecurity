#!/usr/bin/python

import sys
from scapy.all import *

devices = set() #defining a set that holds all MAC addresses of all discoverable WIFI devices

def PacketHandler(pkt): #defining the packet handler that receives the packet as input and ensuring it is a 802.11 packet
	if pkt.haslayer(Dot11) :

		dot11_layer = pkt.getlayer(Dot11)
		if dot11_layer.addr2 and ( dot11_layer.addr2 not in devices ) :
			devices.add(dot11_layer.addr2) 
			print len(devices), dot_11.layer.addr2, dot11_layer.payload.name # prints the number of devices,  MAC addresses, and data frame

sniff(iface = sys.argv[1], count =  int( sys.argv[2] ), prn = PacketHandler)

