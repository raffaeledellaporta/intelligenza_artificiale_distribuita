from distributed_bank_token_ring.config.config import INITIAL_BALANCE, NODE_STATE
from distributed_bank_token_ring.node.atm_node import ATMNode
from distributed_bank_token_ring.node.transaction_manager import init_balance

if __name__ == "__main__":
    init_balance(INITIAL_BALANCE)
    NODE_STATE["ATM4"] = False
    node = ATMNode("ATM4")
    node.transaction = ("withdraw", 500)
    node.start()
