from collections import namedtuple

from src.csv_excel_manager import read_csv_transactions, read_excel_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.utils import load_transactions_from_json
from src.widget import get_date, mask_account_card

FileType = namedtuple("FileType", ["name", "function", "path"])


def get_user_choice(prompt: str, valid_choices: list) -> str:
    """
    :param valid_choices: Список возможных выборов.
    :param prompt: Сообщение, которое будет отображено пользователю для запроса выбора.
    :return: Выбор пользователя
    """
    user_choice = str(input(prompt)).strip().upper()
    while user_choice not in [i.upper() for i in valid_choices]:
        user_choice = str(input(prompt)).strip().upper()
    return user_choice


def main():

    user_answers = dict()

    file_types = {
        "1": FileType("JSON", load_transactions_from_json, "./data/operations.json"),
        "2": FileType("CSV", read_csv_transactions, "./data/transactions.csv"),
        "3": FileType("XLSX", read_excel_transactions, "./data/transactions_excel.xlsx"),
    }

    # получаем тип файла
    user_answers["file_type_choice"] = get_user_choice(
        """
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""",
        file_types.keys(),
    )

    # Сохраняем ответ для чтения данных из файла
    file_type = file_types[user_answers["file_type_choice"]]
    print(f"Для обработки выбран {file_type.name}-файл")

    # Получаем статус 'state'
    user_answers["state_choice"] = get_user_choice(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""",
        ["executed", "canceled", "pending"],
    )

    # Сортировка по дате
    user_answers["sort_by_date_choice"] = get_user_choice("Отсортировать операции по дате? Да/Нет\n", ["ДА", "НЕТ"])
    if user_answers["sort_by_date_choice"] == "ДА":
        user_answers["sort_order_choice"] = get_user_choice(
            "Отсортировать по возрастанию или по убыванию?\n", ["ПО УБЫВАНИЮ", "ПО ВОЗРАСТАНИЮ"]
        )

    # Фильтр по рублю
    user_answers["only_rub_choice"] = get_user_choice("Выводить только рублевые транзакции? Да/Нет\n", ["да", "нет"])

    # Фильтр по слову
    user_answers["search_filter_choice"] = get_user_choice(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n", ["да", "нет"]
    )
    if user_answers["search_filter_choice"] == "ДА":
        user_answers["search_filter_choice"] = str(input("Введите слово: "))

    # # ответы пользователя
    state_choice = user_answers.get("state_choice")
    sort_by_date_choice = user_answers.get("sort_by_date_choice")
    sort_order_choice = user_answers.get("sort_order_choice")
    only_rub_choice = user_answers.get("only_rub_choice")
    search_filter_choice = user_answers.get("search_filter_choice")

    # Путь к файлу и имя функции
    file_path = file_type.path
    file_function = file_type.function

    try:
        # Сохраняем данные из файла в список словарей
        transactions_data = file_function(file_path)

        # Фильтруем список по статусу
        transactions_data = filter_by_state(transactions_data, state_choice)

        # Сортировка по дате
        if sort_by_date_choice == "ДА":
            transactions_data = sort_by_date(transactions_data, sort_order_choice == "ПО УБЫВАНИЮ")

        # Фильтруем по валюте RUB
        if only_rub_choice == "ДА":
            transactions_data = list(filter_by_currency(transactions_data, "RUB"))

        if search_filter_choice != "НЕТ":
            transactions_data = filter_by_description(transactions_data, search_filter_choice.lower())

        # Форматирование данных transaction_data
        if transactions_data:
            print("Распечатываю итоговый список транзакций...")
            print(f"Всего банковских операций в выборке: {len(transactions_data)}\n")

            for transaction in transactions_data:
                print(f"{get_date(transaction['date'])} {transaction['description']}")
                if transaction.get("from") != "" and transaction.get("from") is not None:
                    print(f"{mask_account_card(transaction.get('from'))} -> {mask_account_card(transaction['to'])}")
                else:
                    print(f"{mask_account_card(transaction['to'])}")
                if file_type.name != "JSON":
                    print(f"Сумма: {transaction['amount']} {transaction['currency_name']}\n")
                else:
                    currency_name = transaction.get("operationAmount").get("currency").get("name")
                    amount = transaction.get("operationAmount").get("amount")
                    print(f"Сумма: {amount} {currency_name}\n")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    except Exception as e:
        print(f"Произошла ошибка при обработке файла {file_type.name}: {e}")


if __name__ == "__main__":
    main()
