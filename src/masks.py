import logging
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
log_dir = os.path.join(project_root, "logs")
log_file_path = os.path.join(log_dir, "masks.log")

masks_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file_path, mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """
    :param card_number: Принимает номер карты.
    :return: Возвращает маску номера карты.
    """
    masks_logger.info(f"Вызвана функция get_mask_card_number с номером карты: {card_number}")

    card_number_str = str(card_number)
    if card_number is None or len(card_number_str) != 16:
        masks_logger.error('Неверный номер карты"')
        raise ValueError("Неверный номер карты")
    masked_nums_list = [i for i in range(6, 12)]
    mask = ""
    for i in range(len(card_number_str)):
        if i != 0 and i % 4 == 0:
            mask += " "
        if i in masked_nums_list:
            mask += "*"
        else:
            mask += card_number_str[i]

    masks_logger.info(f"Сгенерирована маска номера карты: {mask}")
    return mask


def get_mask_account(account_number: int) -> str:
    """
    :param account_number: Принимает номер счёта.
    :return: Возвращает маску номера счёта.
    """
    masks_logger.info(f"Вызвана функция get_mask_account с номером счета: {account_number}")

    if account_number is None or len(str(account_number)) != 20:
        masks_logger.error("Неверный номер счета")
        raise ValueError("Неверный номер счета")

    account_number_str = str(account_number)
    masked_account = "**" + account_number_str[-4:]

    masks_logger.info(f"Сгенерирована маска номера счета: {masked_account}")
    return masked_account
