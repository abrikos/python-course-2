import csv
import json
import re
from collections import Counter

import pandas as pd

from src.external_api import get_course
from src.logger import get_logger

log_file = "../logs/utils.log"
logger = get_logger(log_file)


def read_file(file: str) -> str:
    """Чтение фала"""
    try:
        with open(file) as f1:
            logger.debug(f'Read file success: "{file}"')
            return f1.read()
    except FileNotFoundError as e:
        logger.error(e)
        return "[]"


def transaction_sum(tx: dict) -> float:
    """Конвертация суммы транзакции в рубли"""
    course = 1.0
    if tx["operationAmount"]["currency"]["code"] in ("USD", "EUR"):
        course = get_course(tx["operationAmount"]["currency"]["code"])
    logger.debug("TX sum calculated")
    return float(tx["operationAmount"]["amount"]) * course


def read_transactions_json(file: str) -> list:
    """Чтение транзакций из файла JSON"""
    try:
        res = json.loads(read_file(file))
        if type(res) is list:
            logger.debug("Read txs success")
            if len(res) == 0:
                logger.warning(f"Data length: {len(res)}")
            return list(filter(lambda x: all(key in x for key in res[0]), res))
        else:
            logger.warning(f'"{file}" has no list data type ({type(res)})')
            return []
    except json.JSONDecodeError as e:
        logger.error(e)
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
    return list(filter(lambda x: re.search(str(search), x["description"] if x["description"] else '', flags=re.IGNORECASE), transactions))


def count_txs_by_type(transactions: list, states: list) -> dict:
    """Search txs by state"""
    return dict(Counter(map(lambda d: d["state"], filter(lambda d: d["state"] in states, transactions))))
