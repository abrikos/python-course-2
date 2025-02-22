from typing import Generator, List


def card_number_generator(start: int, end: int) -> List:
    """Генератор номеров карт"""
    cards = []
    for num in range(start, end + 1):
        x = str(num).rjust(16, "0")
        chunks, chunk_size = len(x), len(x) // 4
        cards.append(" ".join([x[i : i + chunk_size] for i in range(0, chunks, chunk_size)]))
    return cards


def filter_by_currency(transactions: List, currency: str = "USD") -> filter:
    """Фильтрация транзакций по валюте"""
    return filter(lambda t: t["operationAmount"]["currency"]["name"] == currency, transactions)


def transaction_descriptions(transactions: List) -> Generator:
    """Вывод описания транзакций"""
    for tx in transactions:
        yield tx["description"]
