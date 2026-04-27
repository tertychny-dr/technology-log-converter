# Исходные данные
import json
with open("input.json") as file:
    sensor_data = json.load(file)

# Промежуточная таблица
processed_data = []

# Обработка
for record in sensor_data:
    if record["status"] == "OK":
        temp = record.get("raw_value", 0) / 10
        predbanik = {"id": record["id"], "temp": temp}

        if predbanik["temp"] > 80:
            predbanik["alarm"] = True
        processed_data.append(predbanik)

# Вывод результата в файлы .txt и .json
with open("processed_data.txt", "w", encoding="utf-8") as file:
    for item in processed_data:
        file.write(str(item) + "\n")
    print("Файл processed_data.txt создан")

with open('processed_data.json', 'w') as f:
    f.write(json.dumps(processed_data, indent=2))
    print("Файл processed_data.json создан")