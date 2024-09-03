import json


def load_transactions_from_json(file_path: str) -> list[dict]:
    """
    :param file_path: путь до JSON-файла
    :return: Список словарей с данными о финансовых транзакциях
    """
    with open(file_path, "r") as file:
        transactions_data = json.load(file)
    return transactions_data if type(transactions_data) == list else []
