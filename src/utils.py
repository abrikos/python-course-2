import json
from typing import Any

from src.external_api import get_course


def read_file(file: str) -> str:
    """Чтение фала"""
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError:
        return "[]"


def read_transactions(file: str) -> Any:
    """Чтение транзакций из файла"""
    try:
        return json.loads(read_file(file))
    except json.JSONDecoder:
        return []


def transaction_sum(tx: dict) -> float:
    """Конвертация суммы транзакции в рубли"""
    course = 1.0
    if tx["operationAmount"]["currency"]["code"] in ("USD", "EUR"):
        course = get_course(tx["operationAmount"]["currency"]["code"])
    return float(tx["operationAmount"]["amount"]) * course
