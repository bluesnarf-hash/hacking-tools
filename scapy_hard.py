import scapy.all as scapy

def sniffer(inerface):
	scapy.sniff(iface=inerface,store=False,prn=packetsniff)

def packetsniff(packet):
	print(packet)

sniffer("Wireless LAN adapter Wi-Fi")	
