import matplotlib.pyplot as plt
import numpy as np

# Given data
t = np.arange(1960, 2001, 10)
P = np.array([12600, 14000, 16100, 19100, 23200])

# Create the A matrix
A = np.column_stack((t**2, t, np.ones(t.shape)))

# Calculate x using the least squares solution
x = np.linalg.inv(A.T @ A) @ A.T @ P

# Predict the value of y for t = 2010
t_pred = 2010
y_pred = x[0] * t_pred**2 + x[1] * t_pred + x[2]
print("Predicted value of y for t = 2010:", y_pred)


plt.xlabel('Tempo em anos (t)')
plt.ylabel('Número de bactérias (P)')
plt.scatter(t_pred, y_pred, color='red', label='Valor Previsto')
plt.plot(t, P, 'o', label='Dados Experimentais')
# Calculate the predicted curve
t_curve_pred = np.arange(min(t), t_pred + 1, 10)
y_curve_pred = x[0] * t_curve_pred**2 + x[1] * t_curve_pred + x[2]

# Plot the predicted curve
plt.plot(t_curve_pred, y_curve_pred, color='green', label='Curva Prevista')

plt.legend()
plt.xticks(t)
plt.show()

print("Coefficient matrix:")
print(x)
