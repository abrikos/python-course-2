from typing import List

import pytest
from data_for_testing import transactions

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

card_numbers_checklist = [
    (
        95,
        99,
        [
            "0000 0000 0000 0095",
            "0000 0000 0000 0096",
            "0000 0000 0000 0097",
            "0000 0000 0000 0098",
            "0000 0000 0000 0099",
        ],
    ),
    (33, 34, ["0000 0000 0000 0033", "0000 0000 0000 0034"]),
    (1111222233334444, 1111222233334445, ["1111 2222 3333 4444", "1111 2222 3333 4445"]),
]


@pytest.mark.parametrize("start, end, expected", card_numbers_checklist)
def test_cards_generation(start: int, end: int, expected: List) -> None:
    for i, card_number in enumerate(card_number_generator(start, end)):
        assert card_number == expected[i]


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
