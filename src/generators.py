from typing import Generator, List


def card_number_generator(start: int, end: int) -> Generator:
    """Генератор номеров карт"""
    for num in range(start, end + 1):
        x = str(num).rjust(16, "0")
        chunks, chunk_size = len(x), len(x) // 4
        card = " ".join([x[i : i + chunk_size] for i in range(0, chunks, chunk_size)])
        yield card


def filter_by_currency(transactions: List, currency: str = "USD") -> filter:
    """Фильтрация транзакций по валюте"""
    return filter(lambda t: t["operationAmount"]["currency"]["name"] == currency, transactions)


def transaction_descriptions(transactions: List) -> Generator:
    """Вывод описания транзакций"""
    for tx in transactions:
        yield tx["description"]
