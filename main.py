import asyncio
import threading
from backend.packet_sniffer import start_sniffing
from backend.web_socket import main as websocket_server

def run_sniffer():
    """Runs the packet sniffer in a separate thread."""
    start_sniffing()
    print("Test print from sniffer")

async def main():
    """Runs both the sniffer and WebSocket server concurrently."""
    loop = asyncio.get_running_loop()

    # Run sniffer in a background thread (non-blocking)
    loop.run_in_executor(None, run_sniffer)

    # Start the WebSocket server (async function)
    await websocket_server()

    print("Test print from main loop")  

# Ensure this runs in the main event loop
if __name__ == "__main__":
    asyncio.run(main())  #
