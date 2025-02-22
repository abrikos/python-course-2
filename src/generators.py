from typing import List


def filter_by_currency(transactions: List, currency="USD") -> iter:
    """Фильтрация транзакций по валюте"""
    return filter(lambda t: t["operationAmount"]["currency"]["name"] == currency, transactions)

def transaction_descriptions(transactions: List) ->iter:
    """Вывод описания транзакций"""
    for tx in transactions:
        yield tx["description"]