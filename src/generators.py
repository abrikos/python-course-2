from typing import Generator, List


def filter_by_currency(transactions: List, currency: str = "USD") -> filter:
    """Фильтрация транзакций по валюте"""
    return filter(lambda t: t["operationAmount"]["currency"]["name"] == currency, transactions)


def transaction_descriptions(transactions: List) -> Generator:
    """Вывод описания транзакций"""
    for tx in transactions:
        yield tx["description"]
