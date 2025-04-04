import asyncio
import websockets
import json
from backend.data_processor import aggregate_stats

async def send_data(websocket, path):
    print("Client connected!")
    while True:
        packet_info = {"protocol": "TCP", "size": 100}
        stats = aggregate_stats(packet_info)
        print(f" -> Sending: {stats}")
        await websocket.send(json.dumps(stats))
        await asyncio.sleep(0.5)


async def main():
    async with websockets.serve(send_data, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
