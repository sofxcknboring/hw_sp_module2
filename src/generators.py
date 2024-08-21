from typing import Any, Iterator


def filter_by_currency(transactions_list: list[dict], currency_name: str) -> Iterator[Any]:
    """
    :param transactions_list: Список словарей, представляющих транзакции.
    :param currency_name: Валюта операции.
    :return: Итератор, поочередно выдает транзакции, где валюта соответствует заданной в currency_name.
    """
    return filter(
        lambda transaction: transaction.get("operationAmount").get("currency").get("code") == currency_name,
        transactions_list,
    )


def transaction_descriptions(transactions_list: list[dict]) -> Iterator[str]:
    """
    :param transactions_list: Список словарей, представляющих транзакции.
    :return: Итератор, поочередно выдает описание(description), каждой операции.
    """
    return (transaction["description"] for transaction in transactions_list)


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне.
    """
    card_numbers = [num for num in range(start, end + 1)]

    def get_correct_number(number: int) -> str:
        str_number = "0" * (16 - len(str(number))) + str(number)
        return " ".join(str_number[i : i + 4] for i in range(0, 16, 4))

    return map(get_correct_number, card_numbers)
