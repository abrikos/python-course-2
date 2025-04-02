from datetime import datetime
from typing import Any, Callable

import pandas as pd

import src.utils
from src.utils import add_months


def report_to_file(filename: str = "report.json") -> Callable:
    def decorator(function: Callable) -> Callable:
        def wrapper(*args: tuple, **kwargs: tuple) -> Any:
            try:
                result = function(*args, **kwargs)
                with open(filename, "w") as f:
                    f.write(str(result))
                return result
            except Exception as e:
                print(e)

        return wrapper

    return decorator


fname = "report.log"


@report_to_file(fname)
def spends_by_category(txs: pd.DataFrame, category: str, date: datetime = datetime.now()) -> Any:
    txs_filtered = src.utils.search_txs_by_date(txs, date, add_months(date, 3))
    return sum([x["Сумма операции"] for x in txs_filtered])


spends_by_category(src.utils.get_txs(), "Переводы", datetime(2021, month=12, day=30))
with open(fname) as f:
    print(f.read())
