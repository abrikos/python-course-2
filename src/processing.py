from typing import List


def filter_by_state(dictionaries: List, state: str = 'EXECUTED') -> List:
    return list(filter(lambda item: item['state'] == state, dictionaries))


