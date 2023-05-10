import matplotlib.pyplot as plt
import numpy as np

A = np.array([[1, 1, 1], [1, 2, 4], [1, 3, 9]])
b = np.array([6, 15, 28])

a = np.linalg.solve(A, b)  # A.a = b

print(f"a0 = {a[0]}\na1 = {a[1]}\na2 = {a[2]}")
print("\nO polinômio interpolador é:\n")
print(f"p(t) = {a[0]} + {a[1]} *t + {a[2]} * t^2 \n")

t = np.linspace(0, 5, 100)

(p) = a[0] + a[1] * t + a[2] * t ** 2

x = np.array([1, 2, 3])
y = np.array([6, 15, 28])

plt.scatter(x, y, label='Pontos', color='red')
plt.plot(t, p, label='Polinômio interpolador', color='green')
plt.title('Interpolação polinomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
