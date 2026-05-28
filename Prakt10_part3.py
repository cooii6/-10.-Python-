import json
import matplotlib.pyplot as plt

# Відкриваємо JSON-файл
with open("details.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Словник для підрахунку загальної кількості кожної деталі
details_count = {}

for day_data in data:
    details = day_data["details"]

    for detail_name, detail_info in details.items():
        count = detail_info["count"]

        if detail_name in details_count:
            details_count[detail_name] += count
        else:
            details_count[detail_name] = count

# Дані для кругової діаграми
labels = list(details_count.keys())
values = list(details_count.values())

colors = ["red", "green", "blue", "orange", "purple"]

# Побудова кругової діаграми
plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    colors=colors[:len(labels)],
    startangle=90
)

plt.title("Розподіл виготовлених деталей за кількістю")
plt.legend(labels, title="Деталі", loc="best")

plt.show()