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
