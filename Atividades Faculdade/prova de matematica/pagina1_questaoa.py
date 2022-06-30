n = int(input("Insira o valor de n: "))

# Pagina 1 questão A

print("Pagina 1 questão A\n")

print("Solução por recurção\n")

#A(n+1) - An = 2n + 3 => A(n+1) = 2n + 3 + An
#An = 2(n-1) + 3 + A(n-1)
#A0 = 1


def an(n):
    if n == 0:
        return 1  # A0 da função
    else:

        return (2 * (n-1)) + 3 + (an(n-1))


print(an(n))

print("\nSolução por loop:\n")

an1 = 1 #esse cara aqui é o A0
if n > 0:
    for loop in range(1, (n+1)):
        an1 = (2*(loop-1)) + 3 + an1
print(an1)


print("\nSolução por Solução da Recursão:\n")

def bn(n):
    if n == 0:
        return 1  # A0 da função
    else:

        return (n + 1)**2
print(bn(n))