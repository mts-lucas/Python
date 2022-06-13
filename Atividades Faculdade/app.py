import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
print(x)

plt.figure(figsize=(6, 4))
plt.plot(x, 2*x, color='#17a589', label='f(x) = 2x') # green
plt.plot(x, x/2, color='red', label='f(x) = x/2')
plt.plot(x, x+3, color='#f4d03f', label='f(x) = x + 3') # yellow

plt.grid(True)
plt.title('Retas Simples')
plt.legend()
plt.savefig('reta-titulo-legendas.png')
plt.close()