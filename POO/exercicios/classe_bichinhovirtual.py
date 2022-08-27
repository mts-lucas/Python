# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

#usar isso futuramente prum codigo 

class Tamagushi:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def set_nome(self, novonome):
        self.nome = novonome
    
    def set_fome(self, valorfome):
        self.fome = valorfome

    def set_saude(self, novasaude):
        self.saude = novasaude

    def setIdade(self, novaidade):
        self.idade = novaidade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    def humor(self):
        return self.fome * self.saude
        

b1 = Tamagushi("Pikachu", 5,5,5)

print(b1.humor())