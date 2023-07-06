import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Função que representa o modelo cúbico
def cubic_model(t, B0, B1, B2, B3):
    return B0 + B1 * t + B2 * t**2 + B3 * t**3


# Dados observados
t_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_data = np.array([0, 8.8, 29.9, 62.0, 104.7, 159.1, 222.0,
                  294.5, 380.4, 471.1, 571.7, 686.8, 809.2])

# Encontrar os melhores valores de B0, B1, B2, B3
optimized_params, _ = curve_fit(cubic_model, t_data, y_data)
B0_optimized, B1_optimized, B2_optimized, B3_optimized = optimized_params

# Criar uma série de pontos para plotar a curva ajustada
t_curve = np.linspace(min(t_data), max(t_data), 100)
y_curve = cubic_model(t_curve, B0_optimized, B1_optimized,
                      B2_optimized, B3_optimized)

# Calcular a velocidade quando t = 4.5 segundos
t_estimate = 4.5
velocity_estimate = cubic_model(
    t_estimate, B0_optimized, B1_optimized, B2_optimized, B3_optimized)
print("Valores otimizados:")
print("B0 =", B0_optimized)
print("B1 =", B1_optimized)
print("B2 =", B2_optimized)
print("B3 =", B3_optimized)
print("Velocidade estimada quando t = 4.5 segundos:", velocity_estimate)

# Plotar os dados observados e a curva ajustada
plt.scatter(t_data, y_data, label='Dados Observados')
plt.scatter(4.5, velocity_estimate, label='velocidade esperada em 4.5s')
plt.plot(t_curve, y_curve, 'r', label='Curva Ajustada')
plt.xlabel('Tempo (t)')
plt.ylabel('Posição (y)')
plt.title('Ajuste de Curva Cúbica')
plt.legend()
plt.grid(True)
plt.show()
