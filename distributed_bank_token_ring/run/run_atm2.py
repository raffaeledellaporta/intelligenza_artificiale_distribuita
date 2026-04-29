from distributed_bank_token_ring.node.atm_node import ATMNode

if __name__ == "__main__":
    node = ATMNode("ATM2")
    node.transaction = ("withdraw", 200)
    node.start()
