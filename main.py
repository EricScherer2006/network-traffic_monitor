import asyncio
import threading
from backend.packet_sniffer import start_sniffing
from backend.web_socket import main as websocket_server

def run_sniffer():
    """Runs the packet sniffer in a separate thread."""
    print("Sniffer thread starting")
    start_sniffing()
    print("Sniffer thread started")

async def main():
    """Runs both the sniffer and WebSocket server concurrently."""
    print("Main async loop started")
    loop = asyncio.get_running_loop()

    # Run sniffer in a background thread (non-blocking)
    loop.run_in_executor(None, run_sniffer)
    print("Starting websocket_server")
    # Start the WebSocket server (async function)
    await websocket_server()
    print("Websocket_server started")

# Ensure this runs in the main event loop
if __name__ == "__main__":
    print("Script started")
    asyncio.run(main()) 
    print("Script finished")
