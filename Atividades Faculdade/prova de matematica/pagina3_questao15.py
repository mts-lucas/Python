n = int(input("Insira o valor de n: "))

# Pagina 3 questão 15

print("Pagina 3 questão 15\n")

print("Solução por recurção\n")

#An = 6A(n-1) - 8()
def an(n):
    if n == 0:
        return 1  # A0 da função
    elif n == 1:
        return 0  # A1 da função
    else:

        return (6 * (an(n - 1))) - (8 * (an(n - 2)))


print(an(n))

print("\nSolução por loop:\n")

an0 = 1 #esse cara aqui é o A0
an1 = 0 #esse cara aqui é o A1 (o ultimo termno tbm)

if n >= 2:
    anx = 0
    for loop in range(2, (n+1)):
        anx = an1
        an1 = (6 * an1) - (8 * an0)
        an0 = anx
    print(an1)
elif n == 1:

    print(an1)
    
elif n == 0: 

    print(an0)