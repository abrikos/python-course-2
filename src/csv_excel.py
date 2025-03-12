import csv

import pandas as pd


def read_csv(file: str) -> list:
    """Read txs from CSV"""
    try:
        with open(file) as f:
            return list(csv.reader(f))
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return []


def read_xls(file: str):
    """Read txs from Excel"""
    try:
        return pd.read_excel(file).values.tolist()
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return []


print(read_csv("../data/transactions.csv"))
# print(read_xls("../data/transactions_excel.xlsx"))
