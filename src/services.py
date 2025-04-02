import re

import pandas as pd

import src.utils


def search_person(txs: pd.DataFrame) -> list:
    """Search tx with to/from persons"""
    return list(
        filter(lambda x: x["Категория"] == "Переводы" and re.search(r"\w \d\.", x["Описание"]), txs.to_dict("records"))
    )


search_person(src.utils.get_txs())
