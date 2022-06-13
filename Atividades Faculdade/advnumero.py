import random

print("TENTE ADIVINHAR O NÙMERO")
qj = input("VOCE QUER JOGAR? (s) OU (n): ")


while qj == "s":

    i1 = 1
    numpc = random.randint(1, 100)
    palpites = 0
    lima = 101
    limd = 0
    desc = False

    while i1 <= 10:

        numjog = int(input("Insira um numero de 1 a 100: "))
        if numjog > limd and numjog < lima:

            if i1 == 1 and i1 <= 4 and numjog == numpc:
                print("VOCÊ TEVE MUITA SORTE!")
                i1 = 11
                palpites = palpites + 1

            elif i1 > 4 and i1 <= 7 and numjog == numpc:
                print("VOCÊ JOGA BEM, MAS AINDA CONTOU SORTE")
                i1 = 11
                palpites = palpites + 1

            elif i1 > 7 and numjog == numpc:
                print("VOCÊ É UM EXCELENTE ESTRATEGISTA")
                i1 = 11
                palpites = palpites + 1

            elif numjog > numpc and i1 == 1:
                print("DIGITE UM NÚMERO MENOR")
                i1 = i1 + 1
                palpites = palpites + 1
                lima = numjog

            elif numjog < numpc and i1 == 1:
                print("DIGITE UM NÚMERO MAIOR")
                i1 = i1 + 1
                palpites = palpites + 1
                limd = numjog

            elif numjog > numpc and i1 == 2:
                print("DIGITE UM NÚMERO MENOR")
                i1 = i1 + 1
                palpites = palpites + 1
                lima = numjog

            elif numjog < numpc and i1 == 2:
                print("DIGITE UM NÚMERO MAIOR")
                i1 = i1 + 1
                palpites = palpites + 1
                limd = numjog

            elif numjog > numpc and i1 >= 3 and i1 != 10:
                print("DIGITE UM NÚMERO MENOR")
                i1 = i1 + 1
                palpites = palpites + 1
                lima = numjog

            elif numjog < numpc and i1 >= 3 and i1 != 10:
                print("DIGITE UM NÚMERO MAIOR")
                i1 = i1 + 1
                palpites = palpites + 1
                limd = numjog

            elif numjog != numpc and i1 == 10:
                print("ACABARAM SUAS CHANCES")
                i1 = 11
                palpites = palpites + 1
                desc  = True
        else:
            print("VOCÊ FOi DESCLASSIFICADO")
            i1 = 11
            desc = True 

    print("VOCE USOU {} TENTATIVAS ATÈ O FIM DO JOGO".format(palpites))
    if desc == False:
        if palpites == 1:
            print("SORTE!")
        elif palpites <= 2 and palpites >= 4 and numjog == numpc:
            print("SORTE + ESTRATEGIA")
        elif palpites >= 5 and palpites <= 7 and numjog == numpc:
            print("BOA ESTRATEGIA")
        elif palpites >=8 and palpites <= 10 and numjog == numpc:
            print("PODE MELHORAR")
    elif desc == True:
        print("REPENSAR")

    qj = input("DESEJA CONTINUAR JOGANDO? (s) OU (n): ")

print("FIM DO PROGRAMA")