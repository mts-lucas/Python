import matplotlib.pyplot as plt
import numpy as np


# Função que representa o modelo cúbico
def cubic_model(t, B0, B1, B2, B3):
    return B0 + B1 * t + B2 * t**2 + B3 * t**3


# Dados observados
t_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_data = np.array([0, 8.8, 29.9, 62.0, 104.7, 159.1, 222.0,
                  294.5, 380.4, 471.1, 571.7, 686.8, 809.2])

# Perform matrix manipulation
A = np.column_stack((np.ones_like(t_data), t_data, t_data**2, t_data**3))
b = y_data

# Calculate the parameters using the normal equation
x = np.linalg.inv(A.T @ A) @ A.T @ b
B0_optimized = x[0]
B1_optimized = x[1]
B2_optimized = x[2]
B3_optimized = x[3]

# Create a series of points to plot the fitted curve
t_curve = np.linspace(min(t_data), max(t_data), 100)
y_curve = cubic_model(t_curve, B0_optimized, B1_optimized,
                      B2_optimized, B3_optimized)

# Calculate the velocity when t = 4.5 seconds
t_estimate = 4.5
velocity_estimate = cubic_model(
    t_estimate, B0_optimized, B1_optimized, B2_optimized, B3_optimized)

print("Valores otimizados:")
print("B0 =", B0_optimized)
print("B1 =", B1_optimized)
print("B2 =", B2_optimized)
print("B3 =", B3_optimized)
print("Velocidade estimada quando t = 4.5 segundos:", velocity_estimate)

# Plot the observed data and the fitted curve
plt.scatter(t_data, y_data, label='Dados Observados')
plt.scatter(t_estimate, velocity_estimate, label='Velocidade estimada em 4.5s')
plt.plot(t_curve, y_curve, 'r', label='Curva Ajustada')
plt.xlabel('Tempo (t)')
plt.ylabel('Posição (y)')
plt.title('Ajuste de Curva Cúbica')
plt.legend()
plt.grid(True)
plt.show()
