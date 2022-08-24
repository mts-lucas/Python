#composição: Um classe vai ser dona de objetos de outra classe
#Se a classe principal é apagada todos os objetos nela são apagados tambem


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        
    def inserir_endereco(self, cidade, estado):
        enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(enderco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

