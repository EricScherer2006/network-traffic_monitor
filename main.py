import asyncio
import threading
import logging
from backend.packet_sniffer import start_sniffing
from backend.web_socket import start_websocket_server

stop_sniffer = threading.Event()
logger = logging.getLogger(__name__)


def run_sniffer(stop_event: threading.Event):
    """Blocking sniffer loop, stoppable via threading.Event"""
    try:
        while not stop_event.is_set():
            start_sniffing(timeout=1)
        logger.info("Sniffer stopped")
    except Exception:
        logger.exception("Sniffer crashed")


async def main(stop_event: asyncio.Event):
    loop = asyncio.get_running_loop()

    # Hintergrundthread für Sniffer
    sniffer_future = loop.run_in_executor(None, run_sniffer, stop_sniffer)

    # WebSocket Server starten
    ws_task = asyncio.create_task(start_websocket_server())

    logger.info("Main loop running. Press Ctrl+C to stop")

    try:
        while not stop_event.is_set():
            await asyncio.sleep(0.5)
    finally:
        logger.info("Stopping everything...")
        stop_sniffer.set()
        ws_task.cancel()
        try:
            await ws_task
        except asyncio.CancelledError:
            pass
        # Executor-Task beenden
        await sniffer_future
        logger.info("Main loop exited")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    stop_event = asyncio.Event()

    try:
        asyncio.run(main(stop_event))
    except KeyboardInterrupt:
        print("Ctrl+C pressed! Stopping...")
        stop_event.set()
        stop_sniffer.set()