#1. Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class Bola:

    def __init__(self, cor, material, circunferencia):
        self.cor = cor
        self.material = material
        self.circunferencia = circunferencia

    def troca_cor(self, novacor):
        self.cor = novacor

    def mostra_cor(self):
        return  self.cor


bola1 = Bola("azul", "plastico", "15")
print(bola1.mostra_cor())
bola1.troca_cor("verde")
print(bola1.mostra_cor())