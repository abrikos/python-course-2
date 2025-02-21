from typing import List


def cards_expected() -> List:
    return [
        ("1231 4567 8888 9999", "1231 45** **** 9999"),
        ("RRRR", "Error"),
        ("RRR", "Error"),
        (99, "Error"),
    ]


def account_expected() -> List:
    return [
        ("1231456788889999", "**9999"),
        ("xxx", "Error"),
        (99, "Error"),
    ]


def lists_sort_by_date() -> List:
    return [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ]


def lists_filer_by_state() -> List:
    return [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            ],
            "CANCELED",
            [
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ]
