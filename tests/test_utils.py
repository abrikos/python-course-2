from typing import Any
from unittest.mock import Mock, patch

import src.utils
from src.utils import read_transactions, transaction_sum


@patch("src.utils.get_course")
def test_tx(mock_data: Any) -> None:
    mock_data.return_value = 1
    assert transaction_sum({"operationAmount": {"amount": 55, "currency": {"code": "USD"}}}) == 55


def test_tx_v2() -> None:
    src.utils.get_course = Mock(return_value=1)
    assert transaction_sum({"operationAmount": {"amount": 55, "currency": {"code": "USD"}}}) == 55


def test_read_json() -> None:
    src.utils.read_file = Mock(return_value="[]")
    assert read_transactions("../some/file") == []


def test_read_tx() -> None:
    src.utils.read_file = Mock(return_value="")
    assert read_transactions("../some/file") == []


def test_read_tx2() -> None:
    src.utils.read_file = Mock(return_value="zzzz")
    assert read_transactions("../some/file") == []


def test_read_tx3() -> None:
    src.utils.read_file = Mock(return_value="{}")
    assert read_transactions("../some/file") == []
