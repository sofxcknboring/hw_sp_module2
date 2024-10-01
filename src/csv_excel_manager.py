import csv

import pandas as pd


def read_csv_transactions(file_path: str) -> list[dict] | list:
    """
    Считывает финансовые операции из CSV файла.
    :param file_path: Путь к CSV файлу.
    :return: Список словарей с финансовыми операциями.
    """
    transactions_data = []
    try:
        with open(file_path) as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions_data.append(row)
        return transactions_data
    except FileNotFoundError:
        return []
    except Exception:
        return []


def read_excel_transactions(file_path: str) -> list[dict] | list:
    """
    Считывает финансовые операции из EXCEL файла.
    :param file_path: Путь к EXCEL файлу.
    :return: Список словарей с финансовыми операциями.
    """
    try:
        transactions_df = pd.read_excel(file_path)
        return transactions_df.to_dict(orient="records")
    except FileNotFoundError:
        return []
    except Exception:
        return []
