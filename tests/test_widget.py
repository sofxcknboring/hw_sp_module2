import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        (None, "")
    ],
)
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "account_card",
    [
        "Некорректный ввод",
        "Счет 12345",
        "Card 12345678901234567",
        "Card 1234 5678 9012 3456 7890",
        "Card",
        "Счет ",
    ],
)
def test_mask_account_card_invalid(account_card):
    with pytest.raises(ValueError):
        mask_account_card(account_card)


@pytest.mark.parametrize(
    "date, expected_output",
    [
        ("2023-10-01T12:30:45.123456", "01-10-2023"),
        ("2020-01-01T00:00:00.000000", "01-01-2020"),
        ("1999-12-31T23:59:59.999999", "31-12-1999"),
        ("2000-02-29T12:00:00.000000", "29-02-2000"),
        ("2023-02-28T12:00:00.000000", "28-02-2023"),
    ],
)
def test_get_date(date, expected_output):
    assert get_date(date) == expected_output


@pytest.mark.parametrize(
    "date",
    [
        "Некорректная строка",
        "2023-10-01",
        "2023-10-01T12:30:45",
        "2023-10-01T12:30:45.123456Z",
        "",
    ],
)
def test_get_date_invalid(date):
    with pytest.raises(ValueError):
        get_date(date)
