n = int(input("Insira o valor de n: "))

# Pagina 3 questão 17

print("\nPagina 3 questão 17\n")

print("Solução por recurção\n")

#An = 7A(n-1) - 10A(n-2)

def an(n):
    if n == 1:
        return 16
    elif n == 0:
        return 5
    else:

        return (7 * (an(n - 1))) - (10 * (an(n - 2)))


print(an(n))

print("\nSolução por loop:\n")

an0 = 5 #esse cara aqui é o A0
an1 = 16 #esse cara aqui é o A1 (o ultimo termno tbm)

if n >= 2:
    anx = 0
    for loop in range(2, (n+1)):
        anx = an1
        an1 = (7*an1) - (10*(an0))
        an0 = anx
    print(an1)
elif n == 1:

    print(an1)
    
elif n == 0: 

    print(an0)


print("\nSolução por Solução da Recursão:\n")

def bn(n):
    if n == 0:
        return 5  # A0 da função
    elif n == 1:
        return 16  # A1 da função
    else:

        return ((2) * (5**n)) + (3 * ((2)**n))
print(bn(n))