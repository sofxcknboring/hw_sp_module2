import re
from collections import Counter

from generators import transaction_descriptions


def filter_by_state(bank_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует банковские операции по состоянию.

    :param bank_operations: Список операций (словарей).
    :param state: Состояние для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список операций с заданным состоянием.
    """
    return [i for i in bank_operations if i.get("state") == state]


def sort_by_date(bank_operations: list[dict], sort_order: bool = True) -> list[dict]:
    """
    Сортирует банковские операции по дате.

    :param bank_operations: Список операций (словарей).
    :param sort_order: Условие для сортировки (по умолчанию сортирует по убыванию - True).
    :return: Новый отсортированный список операций
    """
    if bank_operations is None:
        raise ValueError("Не передан список словарей")
    return sorted(bank_operations, key=lambda x: x["date"], reverse=sort_order)


def filter_by_description(bank_operations: list[dict], search_string: str) -> list[dict]:
    """
    Возвращает список операций, у которых в описании есть совпадения со строкой для поиска(search_string).
    :param bank_operations: Список операций (словарей).
    :param search_string: Строка для поиска
    :return: Новый список операций с совпадениями в description
    """
    pattern = re.compile(search_string)
    return [operation for operation in bank_operations if pattern.search(operation["description"])]


def get_counts_by_categories(bank_operations: list[dict], categories: list) -> dict:
    """
    :param bank_operations: Список операций (словарей).
    :param categories: Список категорий
    :return: Словарь, ключи — это названия категорий, значения — это количество операций в каждой категории.
    """
    descriptions = Counter(transaction_descriptions(bank_operations))
    return {category: descriptions.get(category, 0) for category in categories}
