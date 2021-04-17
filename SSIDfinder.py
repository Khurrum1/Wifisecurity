#!/usr/bin/python

import sys
from scapy.all import *

ssid = set()

def PacketHandler(pkt) :

	if pkt.haslayer(Dot11Beacon): #checking if the packet has a beacon frame

		temp = pkt #iterating through the Dot11Elts
		while temp:			
			temp = temp.getlayer(Dot11Elt)	#finding Dot11Elt's
			if temp and temp.ID == 0 and (temp.info not in sssids): #info contains the SSID
				ssids.add(temp.info) #add new found SSID to set
				print len(ssids), pkt.addr3, temp.info
				break 

			temp = temp.payload #moving onto next layer to search for Dot11Elt

sniff(iface = sys.argv[1], count = int (sys.argv[2]), prn = PacketHandler)

