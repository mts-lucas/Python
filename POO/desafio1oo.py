from typing import Union


class Produto:
    def __init__(self, preco: Union[float, int], descricao: str, validade: str):     # noqa: E501
        self.preco: Union[float, int] = preco
        self.descricao: str = descricao
        self.validade: str = validade


class Item:
    def __init__(self, produto: Produto, quantidade: int):
        self.quantidade: int = quantidade
        self.produto: Produto = produto
        self.total: float = self.calcular_total()

    def calcular_total(self):
        return self.produto.preco * self.quantidade


class Venda:
    def __init__(self, data: str, itens: list[Item] = []):
        self.data: str = data
        self.itens: list[Item] = itens
        self.total: float = self.totalizar()

    # com loop for
    # def totalizar(self) -> float:
    #     soma: float = 0.0
    #     for item in self.itens:
    #         soma += item.total
    #     return soma

    def totalizar(self) -> float:
        return sum(map(lambda item: item.total, self.itens))

    def adicionar_item(self, item: Item):
        self.itens.append(item)
        self.total = self.totalizar()

    def exibir_total(self):
        print(f'Total da venda: R$ {round(self.total, 2)}')
