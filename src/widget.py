from dateutil.parser import parse

from src.masks import get_mask_account, get_mask_card_number, validate_account


def mask_account_card(info: str) -> str | bool:
    """Маскирует номер карты или счёта"""
    if not validate_account(info):
        return 'Error'
    card_info = info.split()
    if len(card_info) == 4:
        return get_mask_card_number(info)
    else:
        return get_mask_account(card_info[-1])


def get_date(date: str) -> str:
    """Форматирует дату"""
    try:
        return parse(date).strftime("%d.%m.%Y")
    except ValueError:
        return "Wrong input date"
