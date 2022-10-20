#equação que calcula tempo de impacto de um objeto como chão

print("PRECISAMOS ALETAR A TODOS O TEMPO QUE TEM PARA FUGIR!!\n ")
h = float(input("Por favor insira a altura inicial do meteoro(m): "))
v0 = 0
g = 9.81
import math
t = round((math.sqrt(((2*h)-v0)/g)), 2)
print("Voces tem {}s para fugir!".format(t))
