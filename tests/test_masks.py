import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (4829137601548293, "4829 13** **** 8293"),
        (7392184650123478, "7392 18** **** 3478"),
        (1567894320187654, "1567 89** **** 7654"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_long_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(736541084301358743051233)
    assert str(exc_info.value) == "Неверный номер карты"


def test_short_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(1)
    assert str(exc_info.value) == "Неверный номер карты"


def test_none_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(None)
    assert str(exc_info.value) == "Неверный номер карты"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (73654108430135874305, "**4305"),
        (74756464650135814881, "**4881"),
        (86654108430123271123, "**1123"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_long_mask_account():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(736541084301358743051233)
    assert str(exc_info.value) == "Неверный номер счета"


def test_short_mask_account():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(1)
    assert str(exc_info.value) == "Неверный номер счета"


def test_none_mask_account():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(None)
    assert str(exc_info.value) == "Неверный номер счета"
