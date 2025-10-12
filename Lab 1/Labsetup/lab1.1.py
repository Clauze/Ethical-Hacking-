from scapy.all import *

def print_pkt(pkt):
    pkt.show()
 
pkt =sniff(iface='br-bac3f16481c8',filter='icmp',prn=print_pkt)
