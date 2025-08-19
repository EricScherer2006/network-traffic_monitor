const protocolsList = document.getElementById("protocols-list");
const socket = new WebSocket("ws://localhost:8765");

socket.onopen = () => {
    console.log("WebSocket connected!");
};

socket.onerror = (error) => {
    console.error("WebSocket error:", error);
};

socket.onmessage = (event) => {
    try {
        const data = JSON.parse(event.data);
        const li = document.createElement("li");

        li.className = data.protocol || "ICMP"; // TCP/UDP/ICMP
        li.innerText = `Src: ${data.src} → Dst: ${data.dst} | Protocol: ${data.protocol} | Size: ${data.size} bytes`;

        // Neue Pakete oben hinzufügen
        protocolsList.insertBefore(li, protocolsList.firstChild);

        // Maximal 20 Pakete anzeigen
        if (protocolsList.childNodes.length > 20) {
            protocolsList.removeChild(protocolsList.lastChild);
        }
    } catch (e) {
        console.error("Failed to parse message:", event.data, e);
    }
};
