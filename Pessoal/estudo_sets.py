# sets formam retiram elementos duplicados em iteraveis
#set é um um conjunto que não é  acessavel por indices nem chaves como uma lista ou dic
#funciona basicamente como conjuntos na matematica mesmo


#forma menos comum de se usar:
linguagens = {"Python", "Java", "Python"}
print(linguagens)

#forma mais comum
linguagens3 = {"Python", "Java", "Python"}
set(linguagens3)

print(linguagens3)

#para acessar valores de um set se pode transformar numa lista:

teste = {3, 2, 5, 6, 9, 1 }

# print(teste[0])  essa linha vai dar erro

numeros = list(teste)
print(numeros[0])

# é possivel iterar um set usando for e para saber um indice podemos usar enumarate

for indice, num in enumerate(numeros):
    print(f"{indice}: {num}")