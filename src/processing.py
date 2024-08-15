def filter_by_state(bank_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует банковские операции по состоянию.

    :param bank_operations: Список операций (словарей).
    :param state: Состояние для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список операций с заданным состоянием.
    """
    return [i for i in bank_operations if i["state"] == state]


def sort_by_date(bank_transactions: list[dict], sort_order: bool = True) -> list[dict]:
    """
    Сортирует банковские операции по дате.

    :param bank_transactions: Список операций (словарей).
    :param sort_order: Условие для сортировки (по умолчанию сортирует по убыванию - True).
    :return: Новый отсортированный список операций
    """
    return sorted(bank_transactions, key=lambda x: x["date"], reverse=sort_order)
