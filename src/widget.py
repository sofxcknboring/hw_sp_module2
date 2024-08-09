from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    :param account_card:  Принимает строку, содержащую тип и номер карты или счета.
    :return: Возвращает строку, содержащую тип и замаскированный номер карты или счета.
    """
    account_card_list = account_card.split(" ")
    if len(account_card_list[-1]) == 16:
        card_type = " ".join([i for i in account_card_list if not i.isdigit()])
        return f"{card_type} {get_mask_card_number(int(account_card_list[-1]))}"
    else:
        return f"{account_card_list[0]} {get_mask_account(int(account_card_list[-1]))}"


def get_date(date_string: str) -> str:
    """
    :param date_string: Принимает строку с датой в формате "%Y-%m-%dT%H:%M:%S.%f"
    :return: Возвращает строку с датой в формате "%Y-%m-%d"
    """
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    return date_object.strftime("%Y-%m-%d")
