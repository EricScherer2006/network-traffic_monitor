import asyncio
import websockets
import json
from backend.data_processor import aggregate_stats

async def send_data(websocket, path):
    print("Client connected!")
    while True:
        packet_info = {"protocol": "TCP", "size": 100}
        stats = aggregate_stats(packet_info)
        print(f"➡Sending: {stats}")
        await websocket.send(json.dumps(stats))
        await asyncio.sleep(0.5)

async def start_websocket_server():
    print("Starting WebSocket server at ws://localhost:8765")
    async with websockets.serve(send_data, "0.0.0.0", 8765):
        await asyncio.Future()
