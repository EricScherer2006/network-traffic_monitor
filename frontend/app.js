const protocolsDiv = document.getElementById("protocols");
const socket = new WebSocket("ws://localhost:8765");

socket.onopen = function() {
    console.log("WebSocket connected to frontend JS!");
};
socket.onerror = function(error) {
    console.error("WebSocket caused an error:", error);
};

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    protocolsDiv.innerText = `Protocol: ${data.protocol}, Size: ${data.size} bytes`;
};
