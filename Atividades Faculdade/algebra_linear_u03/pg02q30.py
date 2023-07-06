import matplotlib.pyplot as plt
import numpy as np

sett = [32, 31.9, 31.8, 32.1, 32.2]

for a in sett:
    A = np.array([[-6, 28, 21],
                  [4, -15, -12],
                  [-8, a, 25]])

    polyCarac = np.poly(A)
    r = np.roots(polyCarac)

    t = np.arange(0, 3.1, 0.1)
    p = np.zeros_like(t)
    for i in range(len(t)):
        p[i] = np.linalg.det(A - t[i] * np.eye(A.shape[0]))

    plt.plot(t, p)

plt.show()
