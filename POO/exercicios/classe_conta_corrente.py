# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente():
    def __init__(self, nome, conta, saldo=0):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo

    def alterNome(self, novonome):
        self.nome = novonome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Sua vonta não possui saldo suficiiente para esse saque")
            return 

               
