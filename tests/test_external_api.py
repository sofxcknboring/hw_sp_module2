from unittest.mock import patch

import pytest

from src.external_api import convert_amount_to_rub


@patch("requests.get")
def test_convert_amount_to_rub_success(mock_get):
    transaction = {"operationAmount": {"amount": "100", "currency": {"name": "доллар", "code": "USD"}}}

    mock_get.return_value.json.return_value = {"result": 7500.0}

    assert convert_amount_to_rub(transaction) == 7500.0


def test_convert_amount_to_rub_already_in_rub():
    transaction = {"operationAmount": {"amount": "100", "currency": {"name": "руб.", "code": "RUB"}}}

    result = convert_amount_to_rub(transaction)
    assert result == "100"


def test_convert_amount_to_rub_missing_operation_amount():
    transaction = {}

    with pytest.raises(AttributeError):
        convert_amount_to_rub(transaction)
