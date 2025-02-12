from typing import List

import pytest
from data_for_testing import lists_filer_by_state, lists_sort_by_date

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("data_list, reverse, expected", lists_sort_by_date())
def test_sort_by_date(data_list: List, reverse: bool, expected: List) -> None:
    assert sort_by_date(data_list, reverse) == expected


@pytest.mark.parametrize("data_list, state, expected", lists_filer_by_state())
def test_filter_by_state(data_list: List, state: str, expected: List) -> None:
    assert filter_by_state(data_list, state) == expected
