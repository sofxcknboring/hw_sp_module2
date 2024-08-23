# README

## Цель проекта

Проект предназначен для маскирования номеров банковских карт и счетов, а также для обработки банковских операций.

## Установка

1. Убедитесь, что установлен [Poetry](https://python-poetry.org/).
2. Клонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd <имя_папки_репозитория>
   ```
3. Установите зависимости:
   ```bash
   poetry install
   ```

## Использование

### Маскирование

- **get_mask_card_number(card_number: int) -> str**  
  Маскирует номер карты.
  ```python
  from src.masks import get_mask_card_number
  print(get_mask_card_number(1234567812345678))  # Вывод: 1234 56** **** 5678
  ```

- **get_mask_account(account_number: int) -> str**  
  Маскирует номер счета.
  ```python
  from src.masks import get_mask_account
  print(get_mask_account(1234567890123456))  # Вывод: **3456
  ```

- **mask_account_card(account_card: str) -> str**  
  Маскирует номер карты или счета из строки.
  ```python
  from src.widgets import mask_account_card
  print(mask_account_card("Visa 1234567812345678"))  # Вывод: Visa 1234 56** **** 5678
  ```

### Обработка операций

- **filter_by_state(bank_operations: list[dict], state: str = "EXECUTED") -> list[dict]**  
  Фильтрует операции по состоянию.
  ```python
  from src.processing import filter_by_state
  operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
  ]
  print(filter_by_state(operations))
  # Вывод: [
  #  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
  #  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
  # ]
  ```

- **sort_by_date(bank_transactions: list[dict], sort_order: bool = True) -> list[dict]**  
  Сортирует операции по дате.
  ```python
  from src.processing import sort_by_date
  transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
  ]
  print(sort_by_date(operations))
  # Вывод: [
  #  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
  #  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
  #  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
  #  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
  # ]

  ```
### Генераторы для обработки данных(generators)

- **filter_by_currency(transactions_list: list[dict], currency_name: str) -> Iterator[Any]**  
  Фильтрует список транзакций по заданной валюте.
  ```python
  usd_transactions = filter_by_currency(transactions, "USD")
  for _ in range(2):
      print(next(usd_transactions))

  # Вывод 
  {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
  },
  {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
  },
    ```
- **transaction_descriptions(transactions_list: list[dict]) -> Iterator[str]**

  Возвращает описание транзакции.
  ```python
  descriptions = transaction_descriptions(transactions)
  for _ in range(5):
      print(next(descriptions))

  # Вывод:
  # Перевод организации
  # Перевод со счета на счет
  # Перевод со счета на счет
  # Перевод с карты на карту
  # Перевод организации
  ```
- **card_number_generator(start: int, end: int) -> Iterator[str]**
   
  Генерирует номера карт в заданном диапазоне.
  ```python
  for card_number in card_number_generator(1, 5):
    print(card_number)

  # Вывод: 
  # 0000 0000 0000 0001
  # 0000 0000 0000 0002
  # 0000 0000 0000 0003
  # 0000 0000 0000 0004
  # 0000 0000 0000 0005
  ```
## Тестирование

Чтобы запустить тесты, выполните следующую команду в терминале:

```bash
poetry run pytest
```

## Заключение

Проект предоставляет функции для безопасной работы с банковской информацией.