#getters e setters funcionam como filtros

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual/100)

    # Getter
    @property
    def preco(self):
        return self._preco #no lugar de self.preco é pra ser isso
    
    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str): #esse if verifica se é uma string e etc e tranforma em float
            valor = float(valor.replace("RS", " "))
        self._preco = valor #esse valor vai ser levado pro getter



pd1 = Produto("Camisa", 50)
pd1.desconto(10)
print(pd1.preco)

pd2 = Produto("chinelo", "RS20")
pd2.desconto(15)
print(pd2.preco)


        
