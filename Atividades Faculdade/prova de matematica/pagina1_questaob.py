n = int(input("Insira o valor de n: "))

# Pagina 1 questão B

print("Pagina 1 questão B\n")

print("Solução por recurção\n")

#A(n+1) - An = 3n^2  - n => A(n+1) = 3n^2 - n + An
#An = 3(n-1)^2 - (n-1) + A(n-1)
#A0 = 3


def an(n):
    if n == 0:
        return 3  # A0 da função
    else:

        return (3*((n-1)**2)) - (n-1) + an(n-1)


print(an(n))

print("\nSolução por loop:\n")

an1 = 3 #esse cara aqui é o A0
if n > 0:
    for loop in range(1, (n+1)):
        an1 = (3*((loop-1)**2)) - (loop-1) + an1
print(an1)
