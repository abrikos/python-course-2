import csv
import datetime
import json
import re
from collections import Counter
from typing import Any

import pandas as pd

from src.external_api import get_course


def read_file(file: str) -> str:
    """Чтение фала"""
    try:
        with open(file) as f1:
            return f1.read()
    except FileNotFoundError:
        return "[]"


def transaction_sum(tx: dict) -> float:
    """Конвертация суммы транзакции в рубли"""
    course = 1.0
    if tx["operationAmount"]["currency"]["code"] in ("USD", "EUR"):
        course = get_course(tx["operationAmount"]["currency"]["code"])
    return float(tx["operationAmount"]["amount"]) * course


def read_transactions_json(file: str) -> list:
    """Чтение транзакций из файла JSON"""
    try:
        res = json.loads(read_file(file))
        if type(res) is list:
            return list(filter(lambda x: all(key in x for key in res[0]), res))
        else:
            return []
    except json.JSONDecodeError:
        return []


def read_transactions_csv(file: str) -> list:
    """Read txs from CSV"""
    try:
        with open(file) as f:
            first_line = f.readline().strip().split(";")
            reader = csv.DictReader(f, delimiter=";", fieldnames=first_line, lineterminator="\n")
            tx_list = []
            for row in reader:
                tx_list.append(row)
            return list(filter(lambda x: all(key in x for key in first_line), tx_list))
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return []


def read_transactions_xls(file: str) -> list:
    """Read txs from Excel"""
    try:
        df = pd.read_excel(file)
        keys = df.to_dict("records")[0].keys()
        return list(filter(lambda x: all(key in x for key in keys) and x["id"] > 0, df.to_dict("records")))
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return []


def read_transactions_by_ext(ext: str) -> list:
    """Read transactions from files by extension"""
    file = "../data/transactions." + ext
    match ext:
        case "csv":
            return read_transactions_csv(file)
        case "json":
            return read_transactions_json(file)
        case "xlsx":
            return read_transactions_xls(file)
        case _:
            return []


def search_txs_by_desc(transactions: list, search: str) -> list:
    """Search txs by desc"""
    return list(
        filter(
            lambda x: re.search(str(search), x["description"] if x["description"] else "", flags=re.IGNORECASE),
            transactions,
        )
    )


def search_txs_by_date(txs: pd.DataFrame, start: datetime.date, stop: datetime.datetime) -> list:
    """Search txs by desc"""
    return list(
        filter(
            lambda x: start <= datetime.datetime.strptime(x["Дата операции"], "%d.%m.%Y %H:%M:%S") <= stop
            and type(x["Номер карты"]) is str,
            txs.to_dict("records"),
        )
    )


def count_txs_by_type(transactions: list, states: list) -> dict:
    """Search txs by state"""
    return dict(Counter(map(lambda d: d["state"], filter(lambda d: d["state"] in states, transactions))))


def pretty_object(lst: Any) -> str:
    return json.dumps(lst, indent=2, ensure_ascii=False)


def get_txs() -> pd.DataFrame:
    return pd.read_excel("../data/operations.xlsx")


def get_settings() -> Any:
    return json.loads(read_file("../settings/user_settings.json"))


def add_months(dt: datetime.datetime, months: int = 0) -> datetime.datetime:
    new_month = months + dt.month
    year_inc = 0
    if new_month > 12:
        year_inc += 1
        new_month -= 12
    return dt.replace(month=new_month, year=dt.year + year_inc)
