n = int(input("Insira o valor de n: "))

# Pagina 3 questão 18

print("\nPagina 3 questão 18\n")

print("Solução por recursão\n")

#An = (7A(n-1) - 3A(n-2))/2

def an(n):
    if n == 0 or n == 1:
        return 1
    else:

        return ((7 * (an(n - 1))) - (3 * (an(n - 2))))/2


print(an(n))

print("\nSolução por loop:\n")

an0 = 1 #esse cara aqui é o A0
an1 = 1 #esse cara aqui é o A1 (o ultimo termno tbm)

if n >= 2:
    anx = 0
    for loop in range(2, (n+1)):
        anx = an1
        an1 = ((7*an1) - (3*(an0)))/2
        an0 = anx
    print(an1)
elif n == 1:

    print(an1)
    
elif n == 0: 

    print(an0)


print("\nSolução por Solução da Recursão:\n")

def bn(n):
    if n == 0 or n == 1:
        return 1  # A0 e A1 da função
    else:

        return ((1/5) * (3**n)) + ((4/5) * ((0.5)**n))
print(bn(n))