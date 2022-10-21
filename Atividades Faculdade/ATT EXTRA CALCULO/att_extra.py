import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(1, 11)
# print(x)


# plt.plot(x, 2*x, color='#17a589', label='f(x) = 2x') # green
# plt.plot(x, x/2, color='red', label='f(x) = x/2')
# plt.plot(x, x+3, color='#f4d03f', label='f(x) = x + 3') # yellow



def verifica_tvm(valora, valorb, equacao):
    constn = (valorb - valora) * 1000
    x = np.linspace((valora + 0.001), (valorb - 0.001), num=constn)
    plt.plot(x, equacao, color='red')
    plt.grid(True)
    plt.title('Gráficos')
    plt.legend()
    plt.show()

verifica_tvm(-5, 12, (3*x + 12))