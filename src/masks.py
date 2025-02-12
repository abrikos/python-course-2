import re


def get_mask_card_number(card_number: str) -> str | bool:
    """принимает на вход номер карты и возвращает ее маску"""
    if not type(card_number) is str:
        return False

    if not re.match(r'\d{4} \d{4} \d{4} \d{4}', card_number):
        return False
    return f"{card_number[:4]} {card_number[5:7]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    try:
        return f"**{account_number[-4:]}"
    except TypeError:
        return 'Account mus be string'
