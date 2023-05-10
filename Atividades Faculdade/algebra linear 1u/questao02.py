import matplotlib.pyplot as plt
import numpy as np

velocity = [0, 2, 4, 6, 8, 10]
force = [0, 2.90, 14.8, 39.6, 74.3, 119]

coefficientss = np.polyfit(velocity, force, 5)
polynomial = np.poly1d(coefficientss)

speedEstimated = 750
forceEstimated = polynomial(speedEstimated)

print("O polinômio interpolador é: ")
print(f"\np(t) = {coefficientss[0]:.3f} + {coefficientss[1]:.3f}t^1 + {coefficientss[2]:.3f}t^2 + {coefficientss[3]:.3f}t^3 + {coefficientss[4]:.3f}t^4 + {coefficientss[5]:.3f}t^5")  # noqa: E501

plt.scatter(velocity, force, color='red', label='Medições')
plt.plot(velocity, polynomial(velocity), label='Polinômio Interpolador')
plt.xlabel('Velocidade (100 ft/sec)')
plt.ylabel('Força (100 lb)')
plt.title('Polinômio Interpolador')
plt.legend()
plt.grid(True)
plt.show()
