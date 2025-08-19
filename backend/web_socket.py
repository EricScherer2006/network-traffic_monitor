import asyncio
import websockets
import json
import logging
from backend.packet_sniffer import packet_queue
from backend.data_processor import aggregate_stats

logger = logging.getLogger(__name__)

async def send_data(websocket):
    logger.info("Client connected")
    try:
        while True:
            # Packet aus Queue holen
            try:
                packet_info = packet_queue.get_nowait()
            except Exception:
                await asyncio.sleep(0.1)
                continue

            # Aggregieren
            stats = aggregate_stats(packet_info)
            logger.info(f"➡ Sending via WS: {stats}")
            await websocket.send(json.dumps(stats))
    except websockets.ConnectionClosed:
        logger.error("Client disconnected")

async def start_websocket_server():
    logger.info("Starting WebSocket server at ws://localhost:8765")
    async with websockets.serve(send_data, "0.0.0.0", 8765):
        await asyncio.Future()  # läuft bis cancel
