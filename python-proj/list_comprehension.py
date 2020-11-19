TRANSACTION_TYPES = ["DEPOSIT", "WITHDRAWAL"]
TRANSACTION = "DEPOSIT"

# List comprehension
transaction = next((transaction_type for transaction_type in TRANSACTION_TYPES if transaction_type == TRANSACTION), None)
if transaction is None:
    # raise exception
    pass
print(transaction)

