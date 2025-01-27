from dateutil.parser import parse
from masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счёта"""
    card_info = info.split()
    print(card_info)
    if len(card_info[-1]) == 16:
        card_info[-1] = get_mask_card_number(int(card_info[-1]))
    else:
        card_info[-1] = get_mask_account(int(card_info[-1]))
    return " ".join(card_info)


def get_date(date: str) -> str:
    """Форматирует дату"""
    return parse(date).strftime("%d.%m.%Y")
