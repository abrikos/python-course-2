import re
from operator import itemgetter
from typing import Any

from src import masks, utils, widget

DEBUG = False
yes_no_choice = ["y", "n"]


def check_user_input(values: list, def_value: int | str, number_input: bool = True) -> int | str:
    valid_choices = list(map(lambda x: x + 1, dict(enumerate(values)).keys())) if number_input else values
    error_message = f"Введите значение из {valid_choices if number_input else values}"
    while True:
        try:
            value = def_value if DEBUG else int(input()) if number_input else input()
            if value in valid_choices:
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)


def choose_tx_file(def_value: int) -> list:
    """User choice for file type"""
    file_extensions = ["json", "csv", "xlsx"]
    print("Выберите необходимый пункт меню:\n")
    for idx, ext in enumerate(file_extensions):
        print(f"{idx + 1}. Получить информацию о транзакциях из {ext.upper()}-файла")

    file_type = check_user_input(file_extensions, def_value)
    txs = utils.read_transactions_by_ext(file_extensions[int(file_type) - 1])
    print(f"Для обработки выбран {file_extensions[int(file_type) - 1].upper()} файл. Транзакций: {len(txs)}")
    print()
    return txs


def choose_state(def_value: int) -> str:
    """User choice for filter by state"""
    states = ["EXECUTED", "CANCELED", "PENDING"]
    print("Выберите статус, по которому необходимо выполнить фильтрацию.")
    for idx, state in enumerate(states):
        print(f"{idx + 1}. {state}")
    chosen_state = check_user_input(states, def_value)
    state = states[int(chosen_state) - 1]
    print(f"Выбран фильтр по {state}")
    print()
    return state


def choose_sort_by_date(def_value: str) -> int | str:
    """User choice for sorting"""
    print("Отсортировать операции по дате? y/n")
    return check_user_input(yes_no_choice, def_value, False)


def chose_sort_asc(def_value: int) -> int | str:
    print("Отсортировать по ")
    sort_directions = ["возрастанию", "убыванию"]
    for idx, direction in enumerate(sort_directions):
        print(f"{idx + 1}. {direction}")
    return check_user_input(sort_directions, def_value)


def choose_filter_by_description(def_value: str) -> int | str:
    """User choice for filter"""
    print("Отфильтровать список транзакций по строке в описании? y/n")
    return check_user_input(yes_no_choice, def_value, False)


def choose_word_for_filtration(def_value: str) -> str:
    print("Введите строку для фильтрации")
    return def_value if DEBUG else input()


def choose_rub_txs(def_value: str) -> int | str:
    print("Выводить только рублевые транзакции? y/n")
    return check_user_input(yes_no_choice, def_value, False)


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    txs = choose_tx_file(1)
    state = choose_state(3)
    sort = choose_sort_by_date("y")
    sort_direction = 1
    if sort == "y":
        sort_direction = chose_sort_asc(1)
    filter_by_desc = choose_filter_by_description("y")
    if filter_by_desc == "y":
        word = choose_word_for_filtration("Откр")
        txs = utils.search_txs_by_desc(txs, word)
    rub = choose_rub_txs("y")

    txs_filtered = sorted(
        filter(
            lambda x: x["state"] == state,
            (filter(lambda x: x["currency_code"] == "RUB", txs) if rub == "y" else txs),
        ),
        key=itemgetter("date"),
        reverse=sort_direction == 1,
    )
    print()
    print("---------- Распечатка итогового списка транзакций ----------")
    print(f"Всего банковских операций в выборке: {len(txs_filtered)}")
    # print(json.dumps(txs_chosen, indent=4, ensure_ascii=False))

    for tx in txs_filtered:
        print(widget.format_date(tx["date"]), tx["description"])
        print("Счёт", masks.get_mask_account(tx["to"]))
        print("Сумма", tx["amount"])
        print("Статус", tx["state"])
        print()


main()
