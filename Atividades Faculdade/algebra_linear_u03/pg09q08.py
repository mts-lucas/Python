import numpy as np
import matplotlib.pyplot as plt

# Given data
t = np.arange(1960, 2001, 10)
P = np.array([12600, 14000, 16100, 19100, 23200])

# Create the A matrix
A = np.column_stack((t**2, t, np.ones(t.shape)))

# Calculate x using the least squares solution
x = np.linalg.inv(A.T @ A) @ A.T @ P

plt.xlabel('Tempo em anos (t)')
plt.ylabel('Número de bactérias (P)')
plt.plot(t, P, 'o', label='Dados Experimentais')
plt.plot(t, x[0] * t**2 + x[1] * t + x[2], label='Curva de Ajuste')
plt.legend()
plt.xticks(t)
plt.show()

print("Coefficient matrix:")
print(x)
