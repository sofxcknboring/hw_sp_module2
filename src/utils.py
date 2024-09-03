import json


def load_transactions_from_json(file_path: str) -> list[dict]:
    with open(file_path, 'r') as file:
        transactions_data = json.load(file)
    return transactions_data if type(transactions_data) == list else []

