import uuid

from distributed_bank_token_ring.network.client import send_message
from distributed_bank_token_ring.common.message import Message

if __name__ == "__main__":
    print("[SYSTEM] Invio TOKEN iniziale ad ATM1...")
    token_id = str(uuid.uuid4())

    initial_token_state = {
        "ATM1": False,
        "ATM2": False,
        "ATM3": False,
        "ATM4": False,
        "balance": 1000,
        "token_id": token_id,
    }

    send_message("localhost", 5001, Message("TOKEN", data={
        "token_id": token_id,
        "token_state": initial_token_state,
    }).to_json())

    print("[SYSTEM] TOKEN inviato")