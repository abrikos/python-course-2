from typing import List


def get_mask_card_number(card_number: int) -> str:
    '''принимает на вход номер карты и возвращает ее маску'''
    if len(str(card_number)) != 16:
        return "Wrong card number"
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    '''принимает на вход номер счета и возвращает его маску'''
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"

# print(get_mask_card_number(1234562289606361))
