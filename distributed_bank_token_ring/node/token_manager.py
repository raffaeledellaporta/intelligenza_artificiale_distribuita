from distributed_bank_token_ring.common.logger import LoggerAdapter


class TokenManager:
    def __init__(self, node_id):
        self.node_id = node_id
        self.logger = LoggerAdapter()

    def handle_token(self, node):
        self.logger.info(f"[{self.node_id}] Ricevuto TOKEN")

        if node.has_pending_transaction():
            node.execute_transaction()

        node.forward_token()
