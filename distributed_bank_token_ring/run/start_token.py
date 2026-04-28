from distributed_bank_token_ring.network.client import send_message
from distributed_bank_token_ring.common.message import Message

if __name__ == "__main__":
    print("[SYSTEM] Invio TOKEN iniziale ad ATM1...")
    send_message("localhost", 5001, Message("TOKEN").to_json())
    print("[SYSTEM] TOKEN inviato")