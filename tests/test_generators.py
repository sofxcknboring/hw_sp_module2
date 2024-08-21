import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency_name, expected_values",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
    ],
)
def test_filter_by_currency_valid(transactions, currency_name, expected_values):
    iter_value = filter_by_currency(transactions, currency_name)

    for expected in expected_values:
        assert next(iter_value) == expected

    with pytest.raises(StopIteration):
        next(iter_value)


def test_filter_by_currency_no_currency_name(transactions):
    iter_eur_value = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(iter_eur_value)


def test_filter_by_currency_no_transactions():
    empty_transactions = []
    empty_result = list(filter_by_currency(empty_transactions, "USD"))

    assert empty_result == empty_transactions


def test_transaction_descriptions(transactions):
    result = transaction_descriptions(transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions_no_transactions():
    empty_result = list(transaction_descriptions([]))
    assert empty_result == []


def test_card_number_generator():
    card_numbers = list(card_number_generator(80123456789101, 80123456789105))
    expected = [
        "0080 1234 5678 9101",
        "0080 1234 5678 9102",
        "0080 1234 5678 9103",
        "0080 1234 5678 9104",
        "0080 1234 5678 9105",
    ]
    assert card_numbers == expected


def test_card_number_generator_last_num():
    card_numbers = list(card_number_generator(9999999999999998, 9999999999999999))
    expected = [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ]
    assert card_numbers == expected