from typing import List


def filter_by_state(dictionaries: List, state: str = "EXECUTED") -> List:
    """Фильтрация списков по полю state"""
    return list(filter(lambda item: item["state"] == state, dictionaries))


def sort_by_date(dictionaries: List, reverse: bool = True) -> List:
    """Сортировка списка по дате"""
    return sorted(dictionaries, key=lambda item: item["date"], reverse=reverse)
