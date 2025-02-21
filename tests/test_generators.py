from typing import List

import pytest
from data_for_testing import transactions

from src.generators import filter_by_currency


# @pytest.mark.parametrize("data_list, currency, expected", data_transactions_by_currency())
# def test_filter_by_currency(data_list: List, currency: str, expected: List) -> None:
#    assert filter_by_currency(data_list, currency) == expected


def test_transactions_usd(transactions_fixture_usd: List) -> None:
    iterator = filter_by_currency(transactions, "USD")
    for fixture in transactions_fixture_usd:
        assert next(iterator) == fixture

def test_transactions_undef(transactions_fixture_usd: List) -> None:
    iterator = filter_by_currency(transactions)
    for fixture in transactions_fixture_usd:
        assert next(iterator) == fixture

def test_transactions_rur(transactions_fixture_rur: List) -> None:
    iterator = filter_by_currency(transactions, "RUR")
    for fixture in transactions_fixture_rur:
        assert next(iterator) == fixture
