# Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer
# 0,5 cm.


class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade 
        self.peso = peso 
        self.altura = altura

    def envelhecer(self, novaidade):
        self.idade = novaidade

        if self.idade < 21:
            self.crescer((0.5 * novaidade))

    def engordar(self, novopeso):
        self.peso += novopeso
    
    def emagrecer(self, novopeso):
        self.peso -= novopeso

    def crescer(self, novaltura):
        self.altura += novaltura


