from distributed_bank_token_ring.config.config import INITIAL_BALANCE, NODE_STATE
from distributed_bank_token_ring.node.atm_node import ATMNode
from distributed_bank_token_ring.node.transaction_manager import init_balance

if __name__ == "__main__":
    init_balance(INITIAL_BALANCE)
    NODE_STATE["ATM1"] = False
    node = ATMNode("ATM1")
    node.transaction = ("withdraw", 0)
    node.start()
