from distributed_bank_token_ring.common.logger import LoggerAdapter
from distributed_bank_token_ring.common.message import Message
from distributed_bank_token_ring.config.config import NODES, RING, INITIAL_BALANCE
from distributed_bank_token_ring.network.client import send_message
from distributed_bank_token_ring.network.server import Server


class ATMNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.host, self.port = NODES[node_id]
        self.successor = RING[node_id]
        self.transaction = None
        self.logger = LoggerAdapter()
        self.terminated = False
        self.last_token_id = None
        self.processed_tokens = set()

    def start(self):
        """Avvia il server per ascoltare i messaggi."""
        server = Server(self.host, self.port, self.handle_message)
        server.start()

    def handle_message(self, data):
        """Gestisce l'arrivo del TOKEN."""
        msg = Message.from_json(data)
        if msg.msg_type == "TOKEN":
            token_data = msg.data.get("token_state", {})
            token_id = msg.data.get("token_id")
            self.logger.info(
                f"[{self.node_id}] Token ricevuto - "
                f"ID: {token_id}, Last ID: {self.last_token_id}, Terminated: {self.terminated}"
            )

            if token_id != self.last_token_id:
                self.terminated = False
                self.last_token_id = token_id
            elif token_id in self.processed_tokens:
                self.logger.info(f"[{self.node_id}] Token duplicato ignorato (id: {token_id}).")
                return

            # Registra il token come processato
            self.processed_tokens.add(token_id)

            balance = token_data.get("balance", INITIAL_BALANCE)
            for node in NODES.keys():
                token_data.setdefault(node, False)

            # Aggiorna lo stato locale e controlla le operazioni
            self.logger.info(f"[{self.node_id}] Ricevuto TOKEN con stato: {token_data}")
            if not self.terminated:
                if self.transaction:
                    balance = self.execute_transaction(balance)
                else:
                    self.logger.info(f"[{self.node_id}] Nessuna transazione in coda.")

                # Segnala come completato
                token_data[self.node_id] = True
                token_data["balance"] = balance
                self.terminated = True
                self.logger.info(f"[{self.node_id}] Operazioni completate e segnate nel TOKEN.")

            # Propaga il token al nodo successivo
            self.forward_token(token_data)

    def has_pending_transaction(self):
        """Verifica se ci sono transazioni in sospeso."""
        return self.transaction is not None and not self.terminated

    def execute_transaction(self, balance):
        """Esegue la transazione in coda."""
        t_type, amount = self.transaction
        self.logger.info(f"[{self.node_id}] Inizio transazione: {t_type} {amount}")

        if t_type == "deposit":
            balance += amount
        elif t_type == "withdraw":
            if balance >= amount:
                balance -= amount
            else:
                self.logger.info(f"[{self.node_id}] Fondi insufficienti per prelievo di {amount}.")
                return balance

        self.logger.info(f"[{self.node_id}] Transazione completata. Saldo aggiornato: {balance}")
        self.transaction = (t_type, amount)
        return balance

    def forward_token(self, token_state):
        """Inoltra il token al successivo nodo nell'anello."""
        token_id = token_state.get("token_id")

        if all(token_state.get(node, False) for node in NODES.keys()):
            self.logger.info(f"[{self.node_id}] Tutti i nodi hanno terminato. Arresto del sistema.")
            return

        next_host, next_port = NODES[self.successor]
        msg = Message("TOKEN", data={"token_id": token_id, "token_state": token_state}).to_json()
        send_message(next_host, next_port, msg)

        self.logger.info(f"[{self.node_id}] Inoltrato il TOKEN a {self.successor}. Stato corrente: {token_state}.")
