import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("UNKNOWN", []),
        ("", []),
    ],
)
def test_filter_by_state(bank_operations, state, expected):
    assert filter_by_state(bank_operations, state) == expected


def test_sort_by_date_ascending(bank_operations):
    sorted_operations = sort_by_date(bank_operations, sort_order=False)
    assert sorted_operations == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_descending(bank_operations):
    sorted_operations = sort_by_date(bank_operations, sort_order=True)
    assert sorted_operations == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_with_same_dates():
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-02T00:00:00"},
    ]
    sorted_operations = sort_by_date(operations, sort_order=True)
    assert sorted_operations == [
        {"id": 3, "state": "EXECUTED", "date": "2023-01-02T00:00:00"},
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
    ]


def test_sort_by_date_empty_list():
    assert sort_by_date([]) == []


def test_sort_by_date_invalid_input():
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(None)
    assert str(exc_info.value) == "Не передан список словарей"
