# Associação de classes

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None #atributo que a instancia pode ou não receber

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self): #filtro pra poder interagir com esse atributo 
        return self.__ferramenta

    @ferramenta.setter #configurando o atributo
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta escrevendo")


class MaquinaDeEscrever:
    def escrever(self):
        print("Maquina esta escrevendo")


escritor = Escritor("Lucas")
maquina = MaquinaDeEscrever()
caneta = Caneta("pilot")
escritor.ferramenta = caneta #aqui eu digoq todas as funções da minha classe Caneta agora funcionam dentro dessa instancia de Escritor
escritor.ferramenta.escrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()
