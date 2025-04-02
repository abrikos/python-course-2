from datetime import datetime
from itertools import groupby

import pandas as pd

from src.external_api import get_course, get_stock_prices
from src.logger import get_logger
from src.utils import get_settings, get_txs, pretty_object, search_txs_by_date

log_file = "../logs/views.log"
logger = get_logger(log_file)


def page_home(date: str, txs: pd.DataFrame, settings: dict) -> str:
    """Data for main page"""
    logger.debug("View HP")
    hour = datetime.today().timetuple()[3]
    greeting = (
        "Доброе утро"
        if 6 < hour <= 11
        else "Добрый день" if 11 < hour <= 18 else "Добрый вечер" if 18 < hour <= 22 else "Доброй ночи"
    )
    # print(pretty_object(txs[0]))
    dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    start_of_month = dt.replace(day=1)
    txs_filtered = search_txs_by_date(txs, start_of_month, dt)
    cards = [
        {"last_digits": key, "total_spent": sum(int(item["Сумма операции"]) for item in group)}
        for key, group in groupby(txs_filtered, key=lambda x: x["Номер карты"])
    ]
    for card in cards:
        card["cashback"] = card["total_spent"] / 100 if card["total_spent"] > 0 else 0

    txs_filtered.sort(key=lambda x: x["Сумма операции"], reverse=True)

    # print(pretty_object(settings))
    courses = get_course(",".join(settings["user_currencies"]))
    # print(pretty_object(courses))
    currency_rates = []
    for course in courses["rates"]:
        currency_rates.append({"currency": course, "rate": 1 / courses["rates"][course]})
    # print(pretty_object(currency_rates))
    stocks = get_stock_prices(settings["user_stocks"])
    stock_prices = []
    for stock in stocks:
        stock_prices.append({"stock": stock, "price": stocks[stock]})
    response = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": txs_filtered[:5],
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }
    print(pretty_object(response))
    return pretty_object(response)


page_home("2021-12-02 00:00:00", get_txs(), get_settings())
