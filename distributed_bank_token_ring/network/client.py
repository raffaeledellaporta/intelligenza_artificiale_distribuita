import socket
import time

def send_message(host, port, message):
    for _ in range(5):  # retry
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.send(message.encode())
            client.close()
            return
        except ConnectionRefusedError:
            time.sleep(1)