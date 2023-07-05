import matplotlib.pyplot as plt
import numpy as np

A1 = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
A2 = A1 ** 2
A = np.hstack([A1, A2])
b = np.array([1.8, 2.7, 3.4, 3.8, 3.9]).reshape(-1, 1)

X = np.linalg.inv(A.T @ A) @ A.T @ b
x = np.arange(1.0, 6.0)
plt.plot(x, b, 'o')
x = np.arange(1.0, 5.1, 0.1)
f = X[0] * x + X[1] * (x ** 2)
plt.plot(x, f)

plt.show()
