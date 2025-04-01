import threading
import asyncio
from backend.packet_sniffer import start_sniffing as start_sniffing
from backend.web_socket import main as websocket_server

def run_sniffer():
    start_sniffing()
    print("Test print")


def run_websocket():
    await websocket_server()
    print("Test print")

if __name__ == "__main__":
    sniffer_thread = threading.Thread(target=run_sniffer, daemon=True) 
    sniffer_thread.start()
    
    asyncio.run(run_websocket())
    print("Test print_ from main loop")
