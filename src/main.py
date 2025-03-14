from src import utils

DEBUG = True


def check_user_input(values: list, number_input: bool = True) -> int:
    valid_choices = list(map(lambda x: x + 1, dict(enumerate(values)).keys())) if number_input else values
    error_message = f'Введите значение из {valid_choices if number_input else values}'
    while True:
        try:
            value = 1 if DEBUG else int(input()) if number_input else input()
            if value in valid_choices:
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)


def choose_tx_file() -> list:
    file_extensions = ['json', 'csv', 'xlsx']
    print("Выберите необходимый пункт меню:\n")
    for idx, ext in enumerate(file_extensions):
        print(f"{idx + 1}. Получить информацию о транзакциях из {ext.upper()}-файла\n")

    file_type = check_user_input(file_extensions)
    txs = utils.read_transactions_by_ext(file_extensions[file_type - 1])
    print(f"Для обработки выбран {file_extensions[file_type - 1].upper()} файл. Транзакций: {len(txs)}")
    print()
    return txs


def choose_state() -> str:
    states = ['EXECUTED', 'CANCELED', 'PENDING']
    valid_state_choice = list(map(lambda x: x + 1, dict(enumerate(states)).keys()))
    print("Выберите статус, по которому необходимо выполнить фильтрацию.")
    for idx, state in enumerate(states):
        print(f"{idx + 1}. {state}")
    chosen_state = check_user_input(states)
    state = states[chosen_state - 1]
    print(f'Выбран фильтр по {state}')
    print()
    return state


def choose_sort() -> dict:
    print("Отсортировать операции по дате? y/n")
    yes_no_choice = ['y','n']
    sort = {}
    sort['by_date'] = True if DEBUG else True if check_user_input(yes_no_choice, False)=='y' else False

    print('Отсортировать по ')
    sort_directions = ['возрастанию', "убыванию"]
    for idx, direction in enumerate(sort_directions):
        print(f'{idx+1}. {direction}')
    sort['asc'] = True if DEBUG else True if check_user_input(sort_directions) == 1 else False

    print('Выводить только рублевые транзакции? y/n')
    sort['rub'] = True if DEBUG else True if check_user_input(yes_no_choice, False)=='y' else False

    print('Отфильтровать список транзакций по строке в описании? y/n')
    sort['filter_by_word'] = True if DEBUG else True if check_user_input(yes_no_choice, False)=='y' else False
    if sort['filter_by_word']:
        sort['word'] = 'Открытие' if DEBUG else input('Введите строку для фильтрации\n')
    return sort



def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    txs = choose_tx_file()
    state = choose_state()
    sort = choose_sort()
    print(sort)

main()
