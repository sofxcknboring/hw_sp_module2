import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_amount_to_rub(transaction: dict) -> float:
    """
    Конвертирует валюту в рубли.
    :param transaction: Словарь с данными транзакции.
    :return: Сумма(transaction["amount"]) в рублях.
    """
    try:
        currency = transaction.get("operationAmount").get("currency").get("code")
        amount = transaction.get("operationAmount").get("amount")
    except AttributeError:
        raise AttributeError
    headers = {"apikey": os.getenv("API_KEY")}

    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        response = requests.get(url, headers=headers)
        response_data = response.json()
        return float(response_data["result"])

    return float(amount)
