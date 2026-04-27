# Technology Log Converter

Учебный проект по обработке данных (mini ETL pipeline).

## Описание

Программа обрабатывает входные данные датчиков (список словарей):

- фильтрует записи со статусом "OK"
- вычисляет температуру (raw_value / 10)
- добавляет флаг alarm, если температура > 80

Результат сохраняется в:
- processed_data.txt
- processed_data.json

## Входные данные

Пример:

```json
[
    {"id": 1, "status": "OK"},
    {"id": 2, "raw_value": 850, "status": "OK"},
    {"id": 3, "raw_value": 120, "status": "ERROR"},
    {"id": 4, "raw_value": 920, "status": "OK"},
    {"id": 5, "raw_value": 300, "status": "OK"}
]