import numpy as np
import sympy as sp

for i in range(3, 6):
    J = np.random.randint(1, 11, size=(5, i))
    K = np.random.randint(1, 11, size=(i, 7))
    A = np.dot(J, K)
    esc = sp.Matrix(A).rref()[0]
    C = A[:, :i]
    R = np.array(esc[:i, :])
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
    print(A)
    print("\n")
