# Associação = Usa,  Agregacao = Tem, Composição = É dono, Herança = É


# herança simples

class Pessoa:  # superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse} falando...")


# a herança dos metodos é de cima pra baixo, ou seja as subclasses herdao os metodos e atributos da superclasse mas a superclasse não herda nada delas


class Aluno(Pessoa):  # subclasse
    def estudar(self):
        print(f"{self.nomeclasse} estudando...")


class Cliente(Pessoa):  # subclasse
    def comprar(self):
        print(f"{self.nomeclasse} comprando...")


a1 = Aluno("Lucas", 22)
a1.falar()
a1.estudar()


c1 = Cliente("Vini", 19)
c1.falar()
c1.comprar()
