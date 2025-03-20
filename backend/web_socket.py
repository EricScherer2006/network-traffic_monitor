import asyncio
import websockets
import json
from backend.data_processor import aggregate_stats

async def send_data(websocket, path):
    while True:
        packet_info = {"protocol": "TCP", "size": 100}  # Simulated data
        stats = aggregate_stats(packet_info)
        await websocket.send(json.dumps(stats))
        await asyncio.sleep(0.5)

async def main():
    async with websockets.serve(send_data, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())