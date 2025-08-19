import asyncio
from testing.testdata import start_demo_sniffing
from backend.web_socket import start_websocket_server

async def main():
    # Run websocket server and demo sniffing concurrently
    demo_task = asyncio.create_task(start_demo_sniffing())
    ws_task = asyncio.create_task(start_websocket_server())

    try:
        await asyncio.gather(demo_task, ws_task)
    except KeyboardInterrupt:
        demo_task.cancel()
        ws_task.cancel()
        # Stops blocking from the two tasks
        await asyncio.gather(demo_task, ws_task, return_exceptions=True)
        print("Demo stopped")

if __name__ == "__main__":
    asyncio.run(main())