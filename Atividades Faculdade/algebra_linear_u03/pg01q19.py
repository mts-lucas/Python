import matplotlib.pyplot as plt
import numpy as np


def exponential_func(t, a, b):
    return a * np.exp(b * t)


t = np.array([10, 20, 30, 40, 50])
Nb = np.array([150000, 215000, 335000, 480000, 770000])

params = np.polyfit(t, np.log(Nb), deg=1)
a = np.exp(params[1])
b = params[0]


t_new = np.linspace(10, 60, 100)
N = exponential_func(t_new, a, b)

time = 60
Nb_estimate = exponential_func(time, a, b)
print(
    f"O numero estimado de bacterias aos {time} minutos e {Nb_estimate}")

plt.scatter(t, Nb, label='Dados Originais')
plt.scatter(time, Nb_estimate, label='60 min')
plt.plot(t_new, N, label='Curva de Ajuste')
plt.xlabel('Tempo (t) (min)')
plt.ylabel('Numero de Bacterias (Nb)')
plt.legend()
plt.show()
