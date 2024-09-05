import json
import logging

utils_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def load_transactions_from_json(file_path: str) -> list[dict]:
    """
    :param file_path: принимает путь до JSON-файла
    :return: Список словарей с данными о финансовых транзакциях
    """
    try:
        utils_logger.info(f"Попытка загрузки транзакций из файла: {file_path}")
        with open(file_path, "r") as file:
            transactions_data = json.load(file)

        if isinstance(transactions_data, list):
            utils_logger.info("Транзакции успешно загружены.")
            return transactions_data
        utils_logger.warning("Загруженные данные не являются списком")
        return []
    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
