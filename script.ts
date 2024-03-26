const webSocket = new WebSocket('ws://localhost:8080');

webSocket.onopen = () => {
    console.log('Connection established');
};

webSocket.onmessage = (message) => {
    console.log('Message received:', message.data);
}