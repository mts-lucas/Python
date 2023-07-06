import matplotlib.pyplot as plt
import numpy as np


# Função que representa o modelo d(t)
def descent_model(t, a, b):
    return a * t + b * t**2 * np.exp(-0.1 * t)


# Dados observados
t_data = np.array([5, 10, 15, 20, 25, 30])
d_data = np.array([30, 83, 126, 157, 169, 190])

# Inicialização dos parâmetros

# Cálculo dos parâmetros utilizando mínimos quadrados
A = np.column_stack((t_data, t_data**2 * np.exp(-0.1 * t_data)))
b = d_data

x = np.linalg.inv(A.T @ A) @ A.T @ b
C1_optimized = x[0]
C2_optimized = x[1]

# Curva ajustada
t_curve = np.linspace(min(t_data), max(t_data), 100)
d_curve = descent_model(t_curve, C1_optimized, C2_optimized)

print("Valores otimizados:")
print("C1 =", C1_optimized)
print("C2 =", C2_optimized)

# Plotar os dados observados e a curva ajustada
plt.scatter(t_data, d_data, label='Dados Observados')
plt.plot(t_curve, d_curve, 'r', label='Curva Ajustada')
plt.xlabel('Tempo (t)')
plt.ylabel('Distância de Descida (d)')
plt.title('Modelo de Descida de Paraquedista')
plt.legend()
plt.grid(True)
plt.show()
