from distributed_bank_token_ring.common.logger import LoggerAdapter
from distributed_bank_token_ring.common.message import Message
from distributed_bank_token_ring.config.config import NODES, RING, NODE_STATE
from distributed_bank_token_ring.network.client import send_message
from distributed_bank_token_ring.network.server import Server
from distributed_bank_token_ring.node.token_manager import TokenManager
from distributed_bank_token_ring.node.transaction_manager import deposit, withdraw


class ATMNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.host, self.port = NODES[node_id]
        self.successor = RING[node_id]
        self.token_manager = TokenManager(node_id)
        self.transaction = ("withdraw", 200)
        self.logger = LoggerAdapter()
        self.terminated = False

    def start(self):
        server = Server(self.host, self.port, self.handle_message)
        server.start()

    def handle_message(self, data):
        msg = Message.from_json(data)

        if msg.msg_type == "TOKEN":
            received_state = msg.data.get("NODE_STATE", {})
            NODE_STATE.update(received_state)
            self.logger.info(f"[{self.node_id}] Stato aggiornato di NODE_STATE: {NODE_STATE}")
            self.token_manager.handle_token(self)

    def has_pending_transaction(self):
        return self.transaction is not None and not self.terminated

    def execute_transaction(self):
        t_type, amount = self.transaction

        self.logger.info(f"[{self.node_id}] Inizio transazione {t_type} {amount}")

        if t_type == "deposit":
            new_balance = deposit(amount)
        else:
            _, new_balance = withdraw(amount)

        self.logger.info(f"[{self.node_id}] Saldo aggiornato: {new_balance}")
        self.transaction = None
        self.terminated = True

        NODE_STATE[self.node_id] = True
        self.logger.info(f"[{self.node_id}] Stato del nodo aggiornato {NODE_STATE}")

    def forward_token(self):
        self.logger.info(f"[{self.node_id}] Stato corrente di NODE_STATE: {NODE_STATE}")
        if all(NODE_STATE[node] for node in NODE_STATE):
            self.logger.info(f"[{self.node_id}] Tutti i nodi hanno terminato. Arresto del sistema.")
            return

        next_host, next_port = NODES[self.successor]
        msg = Message("TOKEN", data={"NODE_STATE": NODE_STATE}).to_json()
        send_message(next_host, next_port, msg)

        if self.terminated:
            self.logger.info(
                f"[{self.node_id}] Nodo terminato: inoltro TOKEN a {self.successor} senza eseguire transazioni.")
        else:
            self.logger.info(f"[{self.node_id}] Inviato TOKEN a {self.successor}")
