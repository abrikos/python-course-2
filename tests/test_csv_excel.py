from typing import Any
from unittest.mock import mock_open, patch

import pandas

import src.csv_excel


def test_csv() -> None:
    mock_data = """id;state;date;amount;currency_name;currency_code;from;to;description
10;11;12;13;14;15;16;17;18
20;21;22;23;24;25;26;27;28"""
    with patch("builtins.open", mock_open(read_data=mock_data)):
        assert src.csv_excel.read_csv("fake_file") == [
            {
                "amount": "13",
                "currency_code": "15",
                "currency_name": "14",
                "date": "12",
                "description\n": "18",
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
                "description\n": "28",
                "from": "26",
                "id": "20",
                "state": "21",
                "to": "27",
            }
        ]


@patch("pandas.read_excel")
def test_excel(mock_read_excel: Any) -> None:
    mock_data = pandas.DataFrame([{"id": 1, "state": 2}])
    mock_read_excel.return_value = mock_data
    res = src.csv_excel.read_xls("fake_file")
    assert [{"id": 1, "state": 2}] == res
