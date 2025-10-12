from scapy.all import *
i = 1
while True:  
    pck = IP(dst='8.8.8.8', ttl = i)/ UDP(dport=11443)
    reply = sr1(pck)
    reply.show()

    if reply.type != 11:
        break
    else:
        i+=1
        print(f"ttl {i} reach IP {reply.src}")
        

print(f"finale TTL {i}")
