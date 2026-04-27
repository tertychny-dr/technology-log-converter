# Technology Log Converter

Навчальний проект із обробки даних (mini ETL pipeline).

## Опис

Програма обробляє вхідні дані датчиків (список словників):

- фільтрує записи зі статусом "OK";
- обчислює температуру (raw_value / 10);
- додає флаг alarm, якщо температура > 80.

Результат зберігається в:
- processed_data.txt
- processed_data.json

## Вхідні дані

Приклад:

```json
[
    {"id": 1, "status": "OK"},
    {"id": 2, "raw_value": 850, "status": "OK"},
    {"id": 3, "raw_value": 120, "status": "ERROR"},
    {"id": 4, "raw_value": 920, "status": "OK"},
    {"id": 5, "raw_value": 300, "status": "OK"}
]