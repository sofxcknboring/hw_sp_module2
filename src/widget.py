import re
from typing import Any

from dateutil import parser

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    if account_card is None:
        return ""

    match = re.match(r"(.+?)\s+(\d+)", account_card.strip())
    if match:
        card_type = match.group(1)
        account_number = match.group(2)

        if len(account_number) == 16:
            return f"{card_type} {get_mask_card_number(account_number)}"
        elif len(account_number) == 20:
            return f"{card_type} {get_mask_account(account_number)}"
        else:
            raise ValueError("Неверная длина номера: должен быть 16 или 20 цифр.")

    raise ValueError("Неверный формат входной строки")


def get_date(date_string: str) -> Any:
    """
    :param date_string: Принимает строку с датой в формате ISO 8601.
    :return: Возвращает строку с датой в формате "%Y-%m-%d"
    """
    date_object = parser.isoparse(date_string)
    return date_object.strftime("%d-%m-%Y")
