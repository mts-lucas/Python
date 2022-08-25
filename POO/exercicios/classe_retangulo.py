# . Classe Retangulo: Crie uma classe que modele um retangulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a
# quantidade de pisos e de rodapés necessárias para o local

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def muda_base(self, novabase):
        self.base = novabase
    
    def muda_altura(self, novaaltura):
        self.altura = novaaltura

    def ver_altura(self):
        return self.altura

    def ver_base(self):
        return self.base 
    
    def ver_area(self):
        area = self.base * self.altura
        return area

    def ver_perimetro(self):
        perimetro = (2 *self.base) + (2 * self.altura)
        return perimetro


base = float(input("Insira a base do seu retangulo: "))
alt = float(input("Insira a altura do seu retangulo: "))

r1 = Retangulo(base, alt)
print("A area é: ", r1.ver_area())
print("O perimetro é: ", r1.ver_perimetro())