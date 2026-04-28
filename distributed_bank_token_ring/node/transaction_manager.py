import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BALANCE_FILE = os.path.join(BASE_DIR, "data", "balance.txt")


def init_balance(initial):
    os.makedirs(os.path.dirname(BALANCE_FILE), exist_ok=True)

    if not os.path.exists(BALANCE_FILE) or os.path.getsize(BALANCE_FILE) == 0:
        with open(BALANCE_FILE, "w") as f:
            f.write(str(initial))


def read_balance():
    with open(BALANCE_FILE, "r") as f:
        return int(f.read())


def write_balance(value):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(value))


def deposit(amount):
    balance = read_balance()
    balance += amount
    write_balance(balance)
    return balance


def withdraw(amount):
    balance = read_balance()
    if balance >= amount:
        balance -= amount
        write_balance(balance)
        return True, balance
    return False, balance
