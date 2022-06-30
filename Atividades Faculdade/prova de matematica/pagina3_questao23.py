n = int(input("Insira o valor de n: "))

# Pagina 3 questão 23

print("\nPagina 3 questão 23\n")

print("Solução por Loop\n")


def an(n):
    if n == 0:
        return 6
    elif n == 1:
        return 5
    else:

        return ((6 * an(n-1)) - an(n-2))/9


print(an(n))


print("\nSolução por loop:\n")

an0 = 6 #esse cara aqui é o A0
an1 = 5 #esse cara aqui é o A1 (o ultimo termno tbm)

if n >= 2:
    anx = 0
    for loop in range(2, (n+1)):
        anx = an1
        an1 =  ((6 * an1) - (an0))/9
        an0 = anx
    print(an1)
elif n == 1:

    print(an1)
    
elif n == 0: 

    print(an0)


print("\nSolução por Solução da Recursão:\n")

def bn(n):
    if n == 0:
        return 6  # A0 da função
    elif n == 1:
        return 5  # A1 da função
    else:

        return (3 **(-n))*((9*n) + 6)
print(bn(n))
