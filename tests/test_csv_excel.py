from typing import Any
from unittest.mock import mock_open, patch

import pandas

import src.csv_excel


def test_csv() -> None:
    with patch("builtins.open", mock_open(read_data="a;bc")):
        assert src.csv_excel.read_csv("fake_file") == [["a;bc"]]


@patch("pandas.read_excel")
def test_excel(mock_read_excel: Any) -> None:
    mock_data = pandas.DataFrame({"id": [1, 2, 3], "value": [6, 7, 8]})
    mock_read_excel.return_value = mock_data
    res = src.csv_excel.read_xls("fake_file")
    assert [[1, 6], [2, 7], [3, 8]] == res
