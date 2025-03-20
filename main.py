import threading
from backend.packet_sniffer import start_sniffing as start_sniffing
from backend.web_socket import main as websocket_server

def run_sniffer():
    start_sniffing()
    print("Test print")


def run_websocket():
    websocket_server()
    print("Test print")

if __name__ == "__main__":
    threading.Thread(target=run_sniffer).start()
    threading.Thread(target=run_websocket).start()
    print("Test print")