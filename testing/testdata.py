import asyncio
import random
from backend.packet_sniffer import packet_queue  # reuse the same queue

PROTOCOLS = ["IP" , "TCP" , "UDP" , "ICMP"]

def generate_random_packet():
    return {
        "src": f"192.168.0.{random.randint(1,254)}",
        "dst": f"192.168.0.{random.randint(1,254)}",
        "protocol": random.choice(PROTOCOLS),
        "size": random.randint(40, 1500)
    }

async def start_demo_sniffing(interval=0.3):
    """Simulate continuous packet capturing like the real sniffer."""
    try:
        while True:
            packet = generate_random_packet()
            packet_queue.put(packet)
            await asyncio.sleep(interval)
    except asyncio.CancelledError:
        print("Demo sniffing stopped")