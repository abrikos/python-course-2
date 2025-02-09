from typing import List


def filter_by_state(dictionaries: List, state: str = 'EXECUTED') -> List:
    return list(filter(lambda item: item['state'] == state, dictionaries))


def sort_by_date(dictionaries: List, sort: str = 'ASC') -> List:
    return sorted(dictionaries, key=lambda item: item['date'], reverse=sort != 'ASC')
