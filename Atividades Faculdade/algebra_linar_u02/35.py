import numpy as np
from scipy.linalg import null_space

A = np.array([[7, -9, -4, 5, 3, -3, -7],
              [-4, 6, 7, -2, -6, -5, 5],
              [5, -7, -6, 5, -6, 2, 8],
              [-3, 5, 8, -1, -7, -4, 8],
              [6, -8, -5, 4, 4, 9, 3]])

C = np.hstack((A[:, :2], A[:, 3:4], A[:, 5:6]))
N = np.round(null_space(A), decimals=6)
R = A[:4, :]

M = np.round(null_space(A.T), decimals=4)

S = np.hstack((R.T, N))
T = np.hstack((C, M))

S_inv = np.linalg.inv(S)
T_inv = np.linalg.inv(T)

print("N =", N)
print("\nR =", R)
print("\nM =", M)
print("\nS =", S)
print("\nT =", T)
print("\nS_inv =", S_inv)
print("\nT_inv =", T_inv)
