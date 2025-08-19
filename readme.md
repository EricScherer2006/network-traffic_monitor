# Async Packet Sniffer with WebSocket Streaming

A small Python project that sniffs network packets using `scapy` and streams packet data in real-time over WebSockets. Useful for learning async patterns, queues, and WebSocket servers in Python.

## Features

- Real-time packet sniffing on all available interfaces.
- Async WebSocket server to stream packet data to clients.
- Thread-safe coordination between packet sniffer and async tasks.
- Graceful shutdown on Ctrl+C.

## Requirements

- Python 3.10+
- scapy
- websockets

Install dependencies:

```bash
    pip install -r requirements.txt
```

## Usage

1.Run the Python server:

```bash
python main.py
```

2.Connect a WebSocket client (for example, in a browser console):

const ws = new WebSocket("ws://localhost:8765");
ws.onmessage = (event) => console.log("Packet data:", event.data);

3.Ctrl+C stops both the sniffer and the WebSocket server gracefully.

# Project Structure


backend/
├── packet_sniffer.py
├── web_socket.py
├── data_processor.py  # optional aggregation logic
frontend/  # no frontend yet
main.py
requirements.txt
README.md

# Notes

-Packets are processed from a thread-safe queue and streamed to connected clients.

-The server does not store packets long-term; once sent, they are discarded to avoid memory growth