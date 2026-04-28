import socket
import threading

from distributed_bank_token_ring.common.logger import LoggerAdapter


class Server:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.logger = LoggerAdapter()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.logger.info(f"Server listening on {self.host}:{self.port}")

        try:
            while True:
                conn, _ = self.server_socket.accept()
                threading.Thread(target=self.handle_client, args=(conn,)).start()
        except KeyboardInterrupt:
            self.logger.info("Shutting down server...")
            self.close()

    def handle_client(self, conn):
        data = conn.recv(1024).decode()
        if data:
            self.handler(data)
        conn.close()

    def close(self):
        self.server_socket.close()
