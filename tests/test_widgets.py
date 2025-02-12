from typing import List

import pytest
from test_data import cards_expected, account_expected

from src.widget import get_date, mask_account_card


def test_get_date(dates: List) -> None:
    """Test valid dates with fixture 'dates'"""
    for date in dates:
        assert get_date(date[0]) == date[1]


@pytest.mark.parametrize("card, expected", cards_expected())
def test_cards(card: str, expected: str) -> None:
    """Test card with data from 'test_data.py'"""
    assert mask_account_card(card) == expected


@pytest.mark.parametrize("account, expected", account_expected())
def test_accounts(account: str, expected: str) -> None:
    """Test card with data from 'test_data.py'"""
    assert mask_account_card(account) == expected
