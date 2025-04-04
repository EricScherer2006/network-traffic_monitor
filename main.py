import asyncio
import threading
from backend.packet_sniffer import start_sniffing
from backend.web_socket import start_websocket_server

def run_sniffer():
    """Runs the packet sniffer in a separate thread."""
    try:
        print("Sniffer thread starting")
        start_sniffing()
        print("Sniffer thread started")
    except Exception as e:
        print("Sniffer crashed")

async def main():
    print("Main async function started!") 
    
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, run_sniffer)

    print("About to start WebSocket server...")

    asyncio.create_task(start_websocket_server())  

    print("WebSocket server is running in background!")

    while True:
        await asyncio.sleep(1)
        
# Ensure this runs in the main event loop
if __name__ == "__main__":
    print("Script started")
    asyncio.run(main()) 
    print("Script finished")
