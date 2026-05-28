import numpy as np
import matplotlib.pyplot as plt

# Варіант 8:
# Y(x) = 5 * sin(10*x) * sin(3*x) / sqrt(x), x = [1...7]

x = np.linspace(1, 7, 500)
y = 5 * np.sin(10 * x) * np.sin(3 * x) / np.sqrt(x)

plt.plot(
    x,
    y,
    label="Y(x) = 5*sin(10x)*sin(3x)/sqrt(x)",
    color="red",
    linewidth=2.5,
    linestyle="-"
)

plt.title("Графік функції Y(x)", fontsize=15)
plt.xlabel("x", fontsize=12)
plt.ylabel("Y(x)", fontsize=12)
plt.legend()
plt.grid(True)

plt.show()
