from distributed_bank_token_ring.node.atm_node import ATMNode

if __name__ == "__main__":
    node = ATMNode("ATM3")
    node.transaction = ("deposit", 100)
    node.start()
