# classes que precisam de outras classe são agregadas ex. Concecionaria > Carro > roda

class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_Produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_Produtos(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoDeCompras()
p1 = Produto("Camiseta", 50)
p2 = Produto("Calça", 40)
p3 = Produto("Colar", 10)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)


carrinho.lista_Produtos()
print(carrinho.soma_Produtos())