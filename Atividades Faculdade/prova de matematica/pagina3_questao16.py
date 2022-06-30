n = int(input("Insira o valor de n: "))

#Pagina 3 questão 16

print("\nPagina 3 questão 16\n")

print("Solução por recurção\n")

#An = 2A(n-1) + 8A(n-2)

def an(n):
    if n == 1:
        return 10
    elif n == 0:
        return 4
    else:

        return (2 * (an(n - 1))) + (8 * (an(n - 2)))


print(an(n))

print("\nSolução por loop:\n")

an0 = 4 #esse cara aqui é o A0
an1 = 10 #esse cara aqui é o A1 (o ultimo termno tbm)

if n >= 2:
    anx = 0
    for loop in range(2, (n+1)):
        anx = an1
        an1 = (2*(an1)) + (8*(an0))
        an0 = anx
    print(an1)
elif n == 1:

    print(an1)
    
elif n == 0: 

    print(an0)

print("\nSolução por Solução da Recursão:\n")

def bn(n):
    if n == 0:
        return 4  # A0 da função
    elif n == 1:
        return 10  # A1 da função
    else:

        return ((3) * (4**n)) + (1 * ((-2)**n))
print(bn(n))