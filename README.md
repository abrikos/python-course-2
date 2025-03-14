# Проект "Изучаю Python"

## Описание:

Проект "Изучаю Python" - домашние задания по курсу Skypro Python

## Инструкции по установке

Необходимые зависимости

```poetry python-dateutil```

```poetry python-utils```

```poetry pytest```

```poetry pytest-cov```

## Тестирование
```python -m pytest --cov=src --cov-report=html```

## Модуль utils

```python
def search_txs_by_desc(transactions: list, search: str) -> list:
"""Search txs by desc"""
```
```python
def count_txs_by_type(transactions: list, states: list) -> dict:
    """Search txs by state"""
```
```python
def read_file(file: str) -> str:
    """Чтение фала"""
```
````python
def transaction_sum(tx: dict) -> float:
    """Конвертация суммы транзакции в рубли"""
````
```python
def read_transactions_json(file: str) -> Any:
    """Чтение транзакций из файла JSON"""
```
```python
def read_transactions_csv(file: str) -> list:
    """Read txs from CSV"""
```
```python
def read_transactions_xls(file: str):
    """Read txs from Excel"""
```
```python
def read_transactions_by_ext(ext: str) -> list:
    """Read transactions from files by extension"""
```
```python
def search_txs_by_desc(transactions: list, search: str) -> list:
    """Search txs by desc"""
```
```python
def count_txs_by_type(transactions: list, states: list) -> dict:
    """Search txs by state"""
```


## Модуль decorators
### Декоратор log 
```python
def log(filename=''):
```

## Модуль чтения из CSV и Excel
### Чтение из CSV файла
```python
res = read_csv('path_to_file')
```
### Чтение из Excel файла
```python
res = read_excel('path_to_file')
```

## Модуль generators

### Фильтрация транзакций по валюте:

```python 
def filter_by_currency(transactions: List, currency="USD")->iter
```
Пример использования
```python
usd = transaction_descriptions(transactions)
for tx in transactions:
    print(next(usd))
```

### Вывод описания транзакций:

```python 
def transaction_descriptions(transactions: List) ->iter
```

Пример использования:
```python
iterator = filter_by_currency(transactions)
for tx in transactions:
    print(next(iterator))
```

### Генератор номеров карт
```python
def card_number_generator(start: int, end: int) -> List:
```

Пример использования:
```python
for card_number in card_number_generator(1, 5):
    print(card_number)
```

