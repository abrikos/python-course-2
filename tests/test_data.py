from typing import List


def cards_expected() -> List:
    return [
        ("1231 4567 8888 9999", "1231 45** **** 9999"),
        ("xxx", False),
        (99, False),
    ]

def account_expected() -> List:
    return [
        ("1231456788889999", "**9999"),
        ("xxx", '**xxx'),
        (99, 'Account mus be string'),
    ]


def valid_sort_by_date() -> List:
    return [
        ([
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
         ],
         [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
        ),
    ]
