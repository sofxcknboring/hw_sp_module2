from unittest.mock import mock_open, patch

import pandas as pd

from src.csv_excel_manager import read_csv_transactions, read_excel_transactions


def test_read_csv_transactions_success(mock_csv_data):
    expected_result = [
        {
            "id": "1",
            "state": "EXECUTED",
            "date": "2023-09-05",
            "amount": "100",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Account A",
            "to": "Account B",
            "description": "Transfer",
        },
        {
            "id": "2",
            "state": "PENDING",
            "date": "2023-09-06",
            "amount": "200",
            "currency_name": "EUR",
            "currency_code": "EUR",
            "from": "Account C",
            "to": "Account D",
            "description": "Pending Transfer",
        },
    ]

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = read_csv_transactions("dummy_path.csv")
        assert result == expected_result


def test_read_csv_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_csv_transactions("dummy_path.csv")
        assert result == []


def test_read_csv_transactions_other_exception():
    with patch("builtins.open", side_effect=Exception("Some error")):
        result = read_csv_transactions("dummy_path.csv")
        assert result == []


def test_read_excel_transactions_success(transactions):
    mock_data = transactions
    expected_result = mock_data
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame(mock_data)

        result = read_excel_transactions("dummy_path.xlsx")
        assert result == expected_result


def test_read_excel_transactions_file_not_found():
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = read_excel_transactions("dummy_path.xlsx")
        assert result == []


def test_read_excel_transactions_other_exception():
    with patch("pandas.read_excel", side_effect=Exception):
        result = read_excel_transactions("dummy_path.xlsx")
        assert result == []
