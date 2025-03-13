import csv

import pandas as pd


def read_csv(file: str) -> list:
    """Read txs from CSV"""
    try:
        with open(file) as f:
            first_line = f.readline().split(';')
            reader = csv.DictReader(
                f,
                delimiter=";",
                fieldnames=first_line,
            )
            tx_list = []
            for row in reader:
                tx_list.append(row)
            return tx_list
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return []


def read_xls(file: str):
    """Read txs from Excel"""
    try:
        df = pd.read_excel(file)
        return df.to_dict("records")
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return []


print(read_csv("../data/transactions.csv"))
# print(read_xls("../data/transactions_excel.xlsx"))
