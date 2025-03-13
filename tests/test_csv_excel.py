from typing import Any
from unittest.mock import mock_open, patch

import pandas

import src.csv_excel


def test_csv() -> None:
    with patch("builtins.open", mock_open(read_data="head\n10;11;12;13;14;15;16;17;18")):
        assert src.csv_excel.read_csv("fake_file") == [
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
            }
        ]


@patch("pandas.read_excel")
def test_excel(mock_read_excel: Any) -> None:
    mock_data = pandas.DataFrame([{"id": 1, "state": 2}])
    mock_read_excel.return_value = mock_data
    res = src.csv_excel.read_xls("fake_file")
    assert [{"id": 1, "state": 2}] == res
