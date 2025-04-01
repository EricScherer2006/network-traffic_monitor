from scapy.all import get_if_list
from scapy.all import sniff
import json

def packet_callback(packet):
    print("Package recieved")
    print("✅ Packet received:", packet.summary())
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

def start_sniffing():
    print("Sniffer starting on interface")
    sniff(iface=none, prn=packet_callback, store=False, timeout=5)
    print("Sniffer: Finished")
