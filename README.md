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

## Тестирование

Чтобы запустить тесты, выполните следующую команду в терминале:

```bash
poetry run pytest
```

## Заключение

Проект предоставляет функции для безопасной работы с банковской информацией.