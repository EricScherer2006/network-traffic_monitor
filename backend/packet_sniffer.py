from scapy.all import sniff
import queue
import logging

logger = logging.getLogger(__name__)

packet_queue = queue.Queue()

def packet_callback(packet):
    try:
        packet_info = {
            "src": packet[0][1].src,
            "dst": packet[0][1].dst,
            "protocol": packet[0][1].name,
            "size": len(packet)
        }
        logger.info(f"✅ Packet captured: {packet_info}")
        packet_queue.put(packet_info)
    except Exception as e:
        logger.error(f"Error processing packet: {e}")

def start_sniffing(timeout=1):
    try:
        sniff(iface=None, prn=packet_callback, store=False, timeout=timeout)
    except Exception as e:
        logger.error(f"Sniffer crashed: {e}")