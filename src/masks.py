import logging
import os
import re

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
log_dir = os.path.join(project_root, "logs")
log_file_path = os.path.join(log_dir, "masks.log")

masks_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file_path, mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    :param card_number: Принимает номер карты.
    :return: Возвращает маску номера карты.
    """
    masks_logger.info(f"Вызвана функция get_mask_card_number с номером карты: {card_number}")
    if card_number is not None:
        if re.fullmatch(r"\d{16}", card_number):
            masks_logger.info(f"Сгенерирована маска номера карты: {card_number}")
            masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
            return masked_number
    masks_logger.error("Неверный номер карты")
    raise ValueError("Неверный номер карты")


def get_mask_account(account_number: str) -> str:
    """
    :param account_number: Принимает номер счёта.
    :return: Возвращает маску номера счёта.
    """
    masks_logger.info(f"Вызвана функция get_mask_account с номером счета: {account_number}")
    if account_number is not None:
        if re.fullmatch(r"\d{20}", account_number):
            masks_logger.info(f"Сгенерирована маска номера карты: {account_number}")
            masked_number = "**" + account_number[-4:]
            return masked_number
    masks_logger.error("Неверный номер счета")
    raise ValueError("Неверный номер счета")
