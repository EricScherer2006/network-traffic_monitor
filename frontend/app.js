const protocolsDiv = document.getElementById("protocols");
const socket = new WebSocket("ws://localhost:8765");

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    protocolsDiv.innerText = `Protocol: ${data.protocol}, Size: ${data.size} bytes`;
};