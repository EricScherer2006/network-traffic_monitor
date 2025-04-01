from scapy.all import get_if_list
from scapy.all import sniff
print(get_if_list())
import json

def packet_callback(packet):
    try:
        packet_info = {
            "src": packet[0][1].src,
            "dst": packet[0][1].dst,
            "protocol": packet[0][1].name,
            "size": len(packet)
        }
        print(json.dumps(packet_info))
    except Exception as e:
        print(f"Error processing packet: {e}")

def start_sniffing(interface="\\Device\\NPF_{C141C74E-1825-4155-BE1F-31A720F5F20B}"):
    sniff(iface=interface, prn=packet_callback, store=False)
