import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_course(symbols: str = "USD") -> Any:
    """Получение текущего курса RUB/USD"""
    try:
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base=RUB"
        headers = {"apikey": os.getenv("API_apilayer")}
        response = requests.get(url, headers=headers)
        return response.json()
    except Exception:
        return {"rates": []}


def get_stock_prices(stocks: list) -> Any:
    """Получение текущего курсов S&P500"""
    try:

        url = f"https://api.twelvedata.com/price?symbol={','.join(stocks)}&apikey={os.getenv('API_twelve')}"
        headers = {"Authorization": os.getenv("API_twelve")}
        response = requests.get(url, headers=headers)
        return response.json()
    except Exception as e:
        return {}

#print(get_stock_prices(["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]))