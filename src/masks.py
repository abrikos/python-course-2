import re
from re import Match


def validate_account(account: str) -> Match[str] | None:
    if not type(account) is str:
        return None
    return re.match(r"^\d{4} \d{4} \d{4} \d{4}$|^\d+$", account)


def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if not validate_account(card_number):
        return "Error"
    return f"{card_number[:4]} {card_number[5:7]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if not validate_account(account_number):
        return "Error"
    return f"**{account_number[-4:]}"
