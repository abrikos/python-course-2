from typing import Any
from unittest.mock import Mock, mock_open, patch

import pandas

from src import utils


def test_tx_search_by_description() -> None:
    txs = [{"description": "zzzz"}]
    assert utils.search_txs_by_desc(txs, "aaa") == []
    assert utils.search_txs_by_desc(txs, "z") == txs


def test_tx_counter_by_state() -> None:
    txs = [
        {"state": "a"},
        {"state": "b"},
        {"state": "b"},
    ]
    assert utils.count_txs_by_type(txs, ["a"]) == {"a": 1}
    assert utils.count_txs_by_type(txs, ["a", "b"]) == {"a": 1, "b": 2}


@patch("src.utils.get_course")
def test_tx(mock_data: Any) -> None:
    mock_data.return_value = 1
    assert utils.transaction_sum({"operationAmount": {"amount": 55, "currency": {"code": "USD"}}}) == 55


def test_tx_v2() -> None:
    utils.get_course = Mock(return_value=1)
    assert utils.transaction_sum({"operationAmount": {"amount": 55, "currency": {"code": "USD"}}}) == 55


def test_read_json() -> None:
    utils.read_file = Mock(return_value="[]")
    assert utils.read_transactions_json("../some/file") == []


def test_read_tx() -> None:
    utils.read_file = Mock(return_value="")
    assert utils.read_transactions_json("../some/file") == []


def test_read_tx2() -> None:
    utils.read_file = Mock(return_value="zzzz")
    assert utils.read_transactions_json("../some/file") == []


def test_read_tx3() -> None:
    utils.read_file = Mock(return_value="{}")
    assert utils.read_transactions_json("../some/file") == []


def test_csv() -> None:
    mock_data = """id;state;date;amount;currency_name;currency_code;from;to;description
10;11;12;13;14;15;16;17;18
20;21;22;23;24;25;26;27;28"""
    with patch("builtins.open", mock_open(read_data=mock_data)):
        assert utils.read_transactions_csv("fake_file") == [
            {
                "amount": "13",
                "currency_code": "15",
                "currency_name": "14",
                "date": "12",
                "description": "18",
                "from": "16",
                "id": "10",
                "state": "11",
                "to": "17",
            },
            {
                "amount": "23",
                "currency_code": "25",
                "currency_name": "24",
                "date": "22",
                "description": "28",
                "from": "26",
                "id": "20",
                "state": "21",
                "to": "27",
            },
        ]


@patch("pandas.read_excel")
def test_excel(mock_read_excel: Any) -> None:
    mock_data = pandas.DataFrame([{"id": 1, "state": 2}])
    mock_read_excel.return_value = mock_data
    res = utils.read_transactions_xls("fake_file")
    assert [{"id": 1, "state": 2}] == res
