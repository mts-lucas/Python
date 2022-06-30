n = int(input("Insira o valor de n: "))

# Pagina 1 questão C

print("Pagina 1 questão C\n")

print("Solução por recurção\n")

#A(n+1) - 2An = 2^n => A(n+1) = 2^n + 2An
#An = 2^(n-1) + 2A(n-1)
#A0 = 1


def an(n):
    if n == 0:
        return 1  # A0 da função
    else:

        return (2**(n-1)) + (2*(an(n-1)))  


print(an(n))

print("\nSolução por loop:\n")

an1 = 1 #esse cara aqui é o A0
if n > 0:
    for loop in range(1, (n+1)):
        an1 = (2**(loop-1)) + (2*(an1)) 
print(an1)