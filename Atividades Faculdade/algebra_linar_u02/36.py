import numpy as np
from sympy import Matrix

# Repita o Exercício 35 para uma matriz A de valor 6 x 7 inteiro aleatório cujo
# posto é no máximo 4.


# Crie uma matriz J de valor inteiro aleatório 6 x 4
J = np.random.randint(10, size=(6, 4))
print('Matriz J')
print(np.array(J))

# Crie uma matriz K de valor inteiro aleatório 4 x 7
K = np.random.randint(10, size=(4, 7))
print('Matriz K')
print(np.array(K))

# Defina A = JK
A = np.dot(J, K)
print('Matriz A')
print(np.array(A))

# Calcule o posto de A
posto_A = np.linalg.matrix_rank(A)

# Calcule a forma escalonada reduzida de A usando SymPy
rref_A = Matrix(A).rref()[0]

# Imprima o posto e a forma escalonada reduzida de A
print("Posto de A:", posto_A)
print("Forma escalonada reduzida de A:")
print(np.array(rref_A))
