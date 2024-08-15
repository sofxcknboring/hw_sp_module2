def filter_by_state(bank_operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует банковские операции по состоянию.

    :param bank_operations: Список операций (словарей) с ключом 'state'.
    :param state: Состояние для фильтрации (по умолчанию 'EXECUTED').
    :return: Список операций с заданным состоянием.
    """
    return [i for i in bank_operations if i['state'] == state]



