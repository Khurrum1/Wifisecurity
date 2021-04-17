#!/usr/bin/python

import socket
from scapy.all import *

hidden_ssid_aps = set() #define hidden ssid set

def PacketHandler(pkt) :

	if pkt.haslayer(Dot11Beacon) : #looking for beacon frames to find ssid

		if not pkt.info : 
			if pkt.addr3 not in hidden_ssid_aps : #checking if we have the access point bssid in our list
				hidden_ssid_aps.add(pkt.addr3) 
				print "HIDDEN SSID Network Found! BSSID: ", pkt.addr3 #announcing we have found the hidden ssid network


	elif pkt.haslayer(Dot11ProbeResp) and  ( pkt.addr3 in hidden_ssid_aps ) : #uncovering the hidden ssid, looking for Dot11 proberesponse and address should be in our hidden ssid set
		print "HIDDEN SSID Uncovered! ", pkt.info, pkt.addr3



sniff(iface = sys.argv[1], count = int( sys.argv[2]), prn = PacketHandler)


