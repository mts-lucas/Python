n = int(input("Insira o valor de n: "))

# Pagina 3 questão 22

print("\nPagina 3 questão 22\n")

print("Solução por recursão\n")


def an(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    elif n >= 3:

        return an(n-1) + an(n - 2)
    elif n == 0:
        return


print(an(n))

print("\nSolução por loop:\n")

an1 = 1 #esse cara aqui é o A1
an2 = 3 #esse cara aqui é o A2 (o ultimo termno tbm)

if n >= 2:
    anx = 0
    for loop in range(3, (n+1)):
        anx = an2
        an2 =  an2 + an1
        an1 = anx
    print(an2)
elif n == 1:

    print(an1)
    
elif n == 0: 

    print(None)


# print("\nSolução por Solução da Recursão:\n")

# def bn(n):
#     if n == 1:
#         return 1  # A0 da função
#     elif n == 2:
#         return 3  # A1 da função
#     elif n == 0:
#         return
#     elif n >= 3:
#         return 

# print(bn(n))
