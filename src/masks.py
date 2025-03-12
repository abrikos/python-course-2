import re
from re import Match

from src.logger import get_logger

log_file = "../logs/masks.log"
logger = get_logger(log_file)


def validate_account(account: str) -> Match[str] | None:
    """Валидация строки как банковского счёта"""
    if not type(account) is str:
        logger.error(f"wrong data type {type(account)} - not str")
        return None
    logger.debug(f"{account} is valid")
    return re.match(r"^\d{4} \d{4} \d{4} \d{4}$|^\d+$", account)


def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if not validate_account(card_number):
        return "Error"
    logger.debug("card number was masked")
    return f"{card_number[:4]} {card_number[5:7]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if not validate_account(account_number):
        return "Error"
    logger.debug("account was masked")
    return f"**{account_number[-4:]}"
