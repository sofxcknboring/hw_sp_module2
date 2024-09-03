import json


def load_transactions_from_json(file_path: str) -> list[dict]:
    """
    :param file_path: принимает путь до JSON-файла
    :return: Список словарей с данными о финансовых транзакциях
    """
    try:
        with open(file_path, "r") as file:
            transactions_data = json.load(file)
        return transactions_data if isinstance(transactions_data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
