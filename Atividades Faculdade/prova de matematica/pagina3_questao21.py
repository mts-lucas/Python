n = int(input("Insira o valor de n: "))

# Pagina 3 questão 21

print("\nPagina 3 questão 21\n")

print("Solução por recursão\n")

#An = -8A(n-1) - 16A(n-2)
#A0 = 2   A1 = -20

def an(n):
    if n == 1:
        return (-20)
    elif n == 0:
        return 2
    else:

        return ((-8) * (an(n - 1))) - (16 * (an(n - 2)))


print(an(n))

print("\nSolução por loop:\n")

an0 = 2 #esse cara aqui é o A0
an1 = (-20) #esse cara aqui é o A1 (o ultimo termno tbm)

if n >= 2:
    anx = 0
    for loop in range(2, (n+1)):
        anx = an1
        an1 = ((-8) * an1) - (16 * an0)
        an0 = anx
    print(an1)
elif n == 1:

    print(an1)
    
elif n == 0: 

    print(an0)

print("\nSolução por Solução da Recursão:\n")

def bn(n):
    if n == 0:
        return 2  # A0 da função
    elif n == 1:
        return (-20)  # A1 da função
    else:

        return ((-4)**n)*((3*n) + 2)
print(bn(n))
