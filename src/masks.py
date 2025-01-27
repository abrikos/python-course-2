from typing import List


def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) != 16:
        return "Wrong card number"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number[-4:]}"

# print(get_mask_card_number(1234562289606361))
