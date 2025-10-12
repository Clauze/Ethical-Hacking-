from scapy.all import *

ip = IP()
ip.dst = '10.9.0.6'
ip.src = '10.9.0.5'
ip.iface = 'br-bac3f16481c8'
icmp = ip/ICMP()
icmp.show()
send(icmp)
