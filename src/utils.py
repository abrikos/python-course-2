import json
from typing import Any

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


def read_transactions(file: str) -> Any:
    """Чтение транзакций из файла"""
    try:
        res = json.loads(read_file(file))
        if type(res) is list:
            logger.debug("Read txs success")
            if len(res) == 0:
                logger.warning(f"Data length: {len(res)}")
            return res
        else:
            logger.warning(f'"{file}" has no list data type ({type(res)})')
            return []
    except json.JSONDecodeError as e:
        logger.error(e)
        return []


def transaction_sum(tx: dict) -> float:
    """Конвертация суммы транзакции в рубли"""
    course = 1.0
    if tx["operationAmount"]["currency"]["code"] in ("USD", "EUR"):
        course = get_course(tx["operationAmount"]["currency"]["code"])
    logger.debug("TX sum calculated")
    return float(tx["operationAmount"]["amount"]) * course


# read_transactions("../data/operations2.json")
# with open(log_file) as f:
#    print(f.read())
