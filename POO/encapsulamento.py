#Encapsulamento
#Public, Private, Protected

#se alguem mudar a variavel dados para algo q nao seja um dicionario, quebra completamente a classe, logo é cabivel privar esse parametro



# o _ é equivalente a ao private(algumas linguagens protected), ele não aparece nas indicações mas ainda é possivel acessa-lo
#__ não deixa ser mexido fora da classe, e é convenção entre devs q aquilo não deve ser mexido, mas se alguem tentar o python meio que renomeia esses paremetros usando o nome da classe _BaseDeDados__dados()

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    def Inserir_Clients(self, id, nome):
        if "Clientes" not in self.__dados: 
            self.__dados["Clientes"] = {id: nome}
        else:
            self.__dados["Clientes"].update({id: nome})

    def Apaga_Cliente(self, id):
        if id not in self.__dados["Clientes"]:
            print("Id não existente")
            return
        else: 
            del self.__dados["Clientes"][id]
        

    def Lista_Cliente(self, id, nome):
        for id, nome in self.__dados["Clientes"].items(): #itsms() retorna tuplas com chave e conteudo de um dic
            print(id, nome)

