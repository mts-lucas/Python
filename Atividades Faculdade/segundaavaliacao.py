from math import log

q = " "

while q != "0":

    print("\nSegunda avaliação\n")
    print("Digite o numero da questão (1,2 ou 3) ou 0 para encerrar o programa: ")
    q = input("\nselecione qual questão deseja ver a resposta: ")

    if q == "2":

        print("Questão 2\n")
        print("Calculo do quadrado de um numero")
        j = int(input("Por favor insira um numero: "))
        soma = 0
        for k in range(1, (j + 1)):
            soma += (2 * k) - 1
        print(f"O quadrado de {j} é {soma}")

    if q == "3":

        print("Questão 3\n")
        print("Calculo da idade do seu cachorro\n")
        print("Insira a idade de seu pet em anos e meses")
        anos = float(input("Anos: "))
        meses = float(input("Meses: "))
        idade = anos + (meses/12)
        idadeh = (16*(log(idade))) + 31
        idadefa = int(idadeh)
        idadefm = round((idadeh - (int(idadeh))) * 12)
        if idadefm > 0:
            print(f"A idade humana do seu pet é aproximadamente {idadefa} anos e {idadefm} meses ")
        else:
            print(f"A idade humana do seu pet é aproximadamente {idadefa} anos")

    if q == "1":

        print("Questão 1\n")
        print("Questão 1 letra A\n")
        print(f"linhas - lista: ____, tam = _____, i:   , chave: ____ , k: ____ \n")

        lista = [80, 85, 22, 91, 10]
        print(f"linha 1 - lista: {lista}")
        # print('Lista Inicial:',lista)
        print(f"linha 2 - lista: {lista}")
        tam = len(lista)
        print(f"linha 3 - lista: {lista}, tam = {tam}")
        for i in range(1,tam):
            print(f"linha 4 - lista: {lista}, tam = {tam}, i: {i}")
            chave = lista[i]
            print(f"linha 5 - lista: {lista}, tam = {tam}, i: {i}, chave: {chave}")
            k = i
            print(f"linha 6 - lista: {lista}, tam = {tam}, i: {i}, chave: {chave}, k: {k}")
            while (k > 0) and (chave < lista[k-1]):
                print(f"linha 7 - lista: {lista}, tam = {tam}, i: {i}, chave: {chave}, k: {k}")
                lista[k] = lista[k-1]
                print(f"linha 8 - lista: {lista}, tam = {tam}, i: {i}, chave: {chave}, k: {k}")
                k -= 1
                print(f"linha 9 - lista: {lista}, tam = {tam}, i: {i}, chave: {chave}, k: {k}")
            lista[k] = chave
            print(f"linha 10 - lista: {lista}, tam = {tam}, i: {i}, chave: {chave}, k: {k}")
            # print('i=%d, k=%d, Lista: '%(i,k),lista)
            print(f"linha 11 - lista: {lista}, tam = {tam}, i: {i}, chave: {chave}, k: {k}")
        # print('Lista Final:',lista)
        print(f"linha 12 - lista: {lista}, tam = {tam}, i: {i}, chave: {chave}, k: {k}")

        print("Questão 1 letra B e C\n")

        print("O programa irá verificar os valores de uma lista e ordena-los em ordem crescente, usando o metodo de comparação do valor atual com o valor anterior, e após efetuar a verificação e se nescessario a realocação de posição na lista, sera mostrado o estado atual da lista e de suas variaveis de controle, e ao final do programa sera exibido o resultado final com a lista em ordem crescente") 

print("\nObrigado por corrigir minha avaliação =p")