class Produto:
    def __init__(self, preco, validade, descricao):
        self.preco = preco
        self.descricao = descricao
        self.validade = validade


class Item:
    def __init__(self, produto, quantidade):

        self.quantidade = quantidade
        self.produto = produto
        self.total = self.somar()

    def somar(self):

        return self.produto.preco * self.quantidade


class Venda:
    def __init__(self, data):
        self.data = data
        self.itens = []
        self.total = 0

    def totalizar(self):
        soma = 0
        for item in self.itens:
            soma += item.total

        return soma

    def addItem(self, item):
        self.itens.append(item)
        self.total = self.totalizar()


newProduto = Produto(12, "12/03/2023", "nada")
print(newProduto.preco)

newItem = Item(newProduto, 5)
print(newItem)

newVenda = Venda("12/03/2024")

newVenda.addItem(newItem)
print(newVenda.itens)

print(newVenda.total)
