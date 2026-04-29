NODES = {
    "ATM1": ("localhost", 5001),
    "ATM2": ("localhost", 5002),
    "ATM3": ("localhost", 5003),
    "ATM4": ("localhost", 5004),
}

RING = {
    "ATM1": "ATM2",
    "ATM2": "ATM3",
    "ATM3": "ATM4",
    "ATM4": "ATM1",
}

INITIAL_BALANCE = 1000
