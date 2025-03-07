import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_course(base: str = "USD") -> float:
    """Получение текущего курса RUB/USD"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={base}"
    headers = {"apikey": os.getenv("API")}
    response = requests.get(url, headers=headers)
    return float(response.json()["rates"]["RUB"])
