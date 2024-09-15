import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions_from_json


def test_load_transactions_success():
    mock_data = '[{"amount": "100", "currency": {"name": "руб.", "code": "RUB"}}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions_from_json("dummy_path.json")
        assert result == json.loads(mock_data)


def test_load_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions_from_json("non_existent_file.json")
        assert result == []


def test_load_transactions_not_a_list():
    mock_data = '{"amount": "100", "currency": {"name": "руб.", "code": "RUB"}}'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions_from_json("dummy_path.json")
        assert result == []


def test_load_transactions_empty_list():
    mock_data = '[]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions_from_json("dummy_path.json")
        assert result == json.loads(mock_data)


def test_load_transactions_file_with_spaces():
    mock_data = '   '
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions_from_json("dummy_path.json")
        assert result == []


def test_load_transactions_empty_file():
    mock_data = ''
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions_from_json("dummy_path.json")
        assert result == []


def test_load_transactions_json_decode_error():
    mock_data = '{"amount": "100", "currency": {"name": "руб.", "code": "RUB"'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions_from_json("dummy_path.json")
        assert result == []