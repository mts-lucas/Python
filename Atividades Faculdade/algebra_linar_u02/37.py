import numpy as np
import sympy as sp

A = np.array([[7, -9, -4, 5, 3, -3, -7],
              [-4, 6, 7, -2, -6, -5, 5],
              [5, -7, -6, 5, -6, 2, 8],
              [-3, 5, 8, -1, -7, -4, 8],
              [6, -8, -5, 4, 4, 9, 3]])

esc = sp.Matrix(A).rref()[0]
C = np.hstack((A[:, [0, 1]], A[:, [3]], A[:, [5]]))
R = np.array(esc[:4, :])
CR = np.dot(C, R)

print("A =")
print(A)
print("\nesc =")
print(np.array(esc))
print("\nC =")
print(C)
print("\nR =")
print(R)
print("\nans =")
print(CR)
