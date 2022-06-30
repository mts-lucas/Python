n = int(input("Insira o valor de n: "))

# Pagina 1 questão A

print("Pagina 2\n")

print("Solução por recurção\n")

#An = ((1,06)^n) * A(n-1)
#A0 = 1000


def an(n):
    if n == 0:
        return 1000  # A0 da função
    else:

        return ((1.06 ** (n)) * (an(n-1))) + 200


print(an(n))

print("\nSolução por loop:\n")

an1 = 1000 #esse cara aqui é o A0
if n > 0:
    for loop in range(1, (n+1)):
        an1 = ((1.06 **(loop)) * an1) + 200
print(an1)
