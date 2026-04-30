import socket
import threading

from distributed_bank_token_ring.common.logger import LoggerAdapter


class Server:
    def __init__(self, host, port, handler):
        """
        Inizializza il server TCP.
        Args:
            - host (str): Indirizzo del server (es. "localhost").
            - port (int): Porta su cui ascoltare i messaggi.
            - handler (callable): Funzione chiamata per elaborare i messaggi ricevuti.
        """
        self.host = host
        self.port = port
        self.handler = handler
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.logger = LoggerAdapter()

    def start(self):
        """
        Avvia il server e resta in ascolto per connessioni in entrata.
        """
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
        """
        Gestisce un client connesso al server.
        Args:
            - conn (socket): La connessione con il client.
        """
        data = conn.recv(1024).decode()
        if data:
            self.handler(data)
        conn.close()

    def close(self):
        """
        Chiude il socket del server.
        """
        self.server_socket.close()
