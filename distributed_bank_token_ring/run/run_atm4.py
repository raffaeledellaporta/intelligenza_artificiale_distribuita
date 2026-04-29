from distributed_bank_token_ring.node.atm_node import ATMNode

if __name__ == "__main__":
    node = ATMNode("ATM4")
    node.transaction = ("withdraw", 500)
    node.start()
