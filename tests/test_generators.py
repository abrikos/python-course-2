from typing import List

import pytest
from data_for_testing import transactions

from src.generators import filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("data_list, currency, expected", [([], "", None)])
def test_txs_filter_by_currency_empty(data_list: List, currency: str, expected: object) -> None:
    iterator = filter_by_currency(data_list, currency)
    try:
        assert next(iterator) == expected
    except StopIteration:
        assert True


@pytest.mark.parametrize("data_list, expected", [([], None)])
def test_txs_description_empty(data_list: List, expected: str) -> None:
    iterator = transaction_descriptions(data_list)
    try:
        assert next(iterator) == expected
    except StopIteration:
        assert True


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


def test_transactions_description(transactions_descriptions_fixture: List) -> None:
    iterator = transaction_descriptions(transactions)
    for fixture in transactions_descriptions_fixture:
        assert next(iterator) == fixture
