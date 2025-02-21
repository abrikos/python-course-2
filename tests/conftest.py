from datetime import datetime
from typing import List

import pytest
from tests.data_for_testing import transactions


@pytest.fixture
def dates() -> List:
    return [
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
        ("20", f'20.{datetime.now().strftime("%m")}.{datetime.now().year}'),
        ("20.03", f'20.{datetime.now().strftime("%m")}.{datetime.now().year}'),
        ("20.03", f'20.{datetime.now().strftime("%m")}.{datetime.now().year}'),
        ("20-00-12", "Wrong input date"),
        ("text", "Wrong input date"),
    ]


@pytest.fixture
def transactions_fixture_usd() -> List:
    return [{
        "id": 1,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }, {
        "id": 3,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "300",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
    ]


@pytest.fixture
def transactions_fixture_rur() -> List:
    return [
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "200",
                "currency": {
                    "name": "RUR",
                    "code": "RUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 4,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "400",
                "currency": {
                    "name": "RUR",
                    "code": "RUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]
