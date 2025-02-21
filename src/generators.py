from typing import List


def filter_by_currency(transactions: List, currency="USD") -> iter:
    return filter(lambda t: t["operationAmount"]["currency"]["name"] == currency, transactions)
