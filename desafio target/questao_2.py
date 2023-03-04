# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
# sempre será a soma dos 2 valores anteriores (ex: 0, 1, 1, 2, 3, 5, 8...),
# escreva um programa na linguagem que desejar onde, informado um número, ele
# calcule a sequência de Fibonacci e retorne uma mensagem avisando se o
# número informado pertence ou não a sequência.


# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua
# preferência ou pode ser previamente definido no código;

def isNumberInFibonacci(number):

    penult = 0
    last = 1
    fibo = [penult, last]

    while (last <= number):
        newlast = last + penult
        fibo.append(newlast)
        penult = last
        last = newlast

    for x in fibo:
        if x == number:

            print(f'{number} is in the fibonacci sequence')
            break

        elif x > number:

            print(f'{number} is not in the fibonacci sequence')
            break


isNumberInFibonacci(50)
