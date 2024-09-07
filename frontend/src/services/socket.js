import { io } from "socket.io-client";

const SOCKET_URL = process.env.REACT_APP_SOCKET_URL;
let socket;

export const initiateSocketConnection = () => {
  socket = io(SOCKET_URL);
  console.log('Connecting to Socket.IO server at', SOCKET_URL);
  socket.on('connect', () => {
    console.log('Socket connected:', socket.id);
  });
  socket.on('connect_error', (err) => {
    console.error('Socket connection error:', err);
  });
};

export const subscribeToUpdates = (cb) => {
  if (!socket) return;
  socket.on('update', (data) => {
    console.log('Received update:', data);
    cb(data);
  });
};

export const disconnectSocket = () => {
  if (socket) {
    console.log('Disconnecting socket:', socket.id);
    socket.disconnect();
  }
};