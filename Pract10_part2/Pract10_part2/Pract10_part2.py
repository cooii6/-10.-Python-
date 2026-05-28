import pandas as pd
import matplotlib.pyplot as plt

# Зчитування даних з CSV файлу
data = pd.read_csv("worldbank_data.csv")

years = data["Year"]
ukraine = data["Ukraine"]
albania = data["Albania"]

# Завдання 2.1 - побудова двох графіків на одній координатній осі
plt.plot(years, ukraine, label="Ukraine", color="purple", linewidth=2)
plt.plot(years, albania, label="Albania", color="orange", linewidth=2)

plt.title("Population, ages 7-11, total", fontsize=15)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Indicator value(100k)", fontsize=12)
plt.legend()
plt.grid(True)

plt.show()

# Завдання 2.2 - стовпчаста діаграма для країни, яку вводить користувач
print("Доступні країни: Ukraine, Albania")
country = input("Введіть назву країни: ")

if country in data.columns:
    plt.bar(years, data[country], color="green")

    plt.title(f"Population, ages 7-11, total - {country}", fontsize=15)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Indicator value", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y")

    plt.show()
else:
    print("Такої країни немає у CSV файлі.")