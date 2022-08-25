# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

from traceback import print_tb


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def muda_lado(self, novolado):
        self.lado = novolado

    def retorna_lado(self):
        return self.lado

    def calcula_area(self):
        area = self.lado * self.lado
        return area

qd = Quadrado(5)
print(qd.lado)
print(qd.calcula_area())
qd.muda_lado(2)
print(qd.lado)
print(qd.calcula_area())

