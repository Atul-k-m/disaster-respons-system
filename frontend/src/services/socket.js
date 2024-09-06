import { io } from "socket.io-client";

const SOCKET_URL = process.env.REACT_APP_SOCKET_URL;
let socket;

export const initiateSocketConnection = () => {
  socket = io(SOCKET_URL);
  console.log('Connecting to Socket.IO server...');
};

export const subscribeToUpdates = (cb) => {
  if (!socket) return;
  socket.on('update', (data) => {
    console.log('Received update:', data);
    cb(data);
  });
};

export const disconnectSocket = () => {
  if (socket) socket.disconnect();
};
