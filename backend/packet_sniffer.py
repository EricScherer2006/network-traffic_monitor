from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

import queue
import logging

logger = logging.getLogger(__name__)

packet_queue = queue.Queue()

def packet_callback(packet):
    try:
        if IP in packet:
            ip_layer = packet[IP]
            protocol = "OTHER"
            if TCP in packet:
                protocol = "TCP"
            elif UDP in packet:
                protocol = "UDP"
            elif ICMP in packet:
                protocol = "ICMP"
            elif IP in packet:
                protocol = "IP"

            packet_info = {
                "src": ip_layer.src,
                "dst": ip_layer.dst,
                "protocol": protocol,
                "size": len(packet)
            }

        else:
            return

        logger.info(f"✅ Packet captured: {packet_info}")
        packet_queue.put(packet_info)
    except Exception as e:
        logger.error(f"Error processing packet: {e}")

def start_sniffing(timeout=1):
    try:
        sniff(iface=None, prn=packet_callback, store=False, timeout=timeout)
    except Exception as e:
        logger.error(f"Sniffer crashed: {e}")