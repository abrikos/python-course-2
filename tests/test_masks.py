from typing import List

import pytest
from test_data import cards_expected,account_expected

from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("card, expected", cards_expected())
def test_cards(card: str, expected: str) -> None:
    assert get_mask_card_number(card) == expected

@pytest.mark.parametrize("account, expected", account_expected())
def test_accounts(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected
