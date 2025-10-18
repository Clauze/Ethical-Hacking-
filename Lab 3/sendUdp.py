#!/bin/env python3
  
from scapy.all import IP, UDP, send, Raw
from ipaddress import IPv4Address
from random import getrandbits
ip = IP(dst="10.9.0.11")
udp = UDP(dport=8080)

for x in range(100):
    pkt = ip/udp/Raw("echo hello "+str(x))
    pkt[IP].src = str(IPv4Address(getrandbits(32)))  # source iP
    send(pkt, verbose = 0)
print("Complete")

