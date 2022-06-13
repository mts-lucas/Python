# Experimente usar outras estratégias de
# repetição:
# a. Disputar 5 partidas e identificar quantas
# partidas cada jogador venceu,
# apresentando inclusive o número de
# empates
# b. Disputar várias partidas até que um dos
# jogadores obtenha 5 vitórias
# c. Disputar várias partidas até que um dos
# jogadores obtenha 3 vitórias seguidas.
# No caso de ocorrer um empate, deve-se
# zerar a contagem

import random
ptj = 0
ptc = 0
ept = 0
partidas = 0
while (ptj < 3) and (ptc < 3):
    jog1 = random.randint(1, 6)
    comp1 = random.randint(1, 6)
    jog2 = random.randint(1, 6)
    comp2 = random.randint(1, 6)

    # rolagens do jogador

    if (jog1 == 1):
        print("primeiro dado jogador")
        print(".......")
        print(".     .")
        print(".  .  .")
        print(".     .")
        print(".......")
    if (jog1 == 2):
        print("primeiro dado jogador")
        print(".......")
        print("..    .")
        print(".     .")
        print(".    ..")
        print(".......")
    if (jog1 == 3):
        print("primeiro dado jogador")
        print(".......")
        print("..    .")
        print(".  .  .")
        print(".    ..")
        print(".......")
    if (jog1 == 4):
        print("primeiro dado jogador")
        print(".......")
        print("..   ..")
        print(".     .")
        print("..   ..")
        print(".......")
    if (jog1 == 5):
        print("primeiro dado jogador")
        print(".......")
        print("..   ..")
        print(".  .  .")
        print("..   ..")
        print(".......")
    if (jog1 == 6):
        print("primeiro dado jogador")
        print(".......")
        print("..   ..")
        print("..   ..")
        print("..   ..")
        print(".......")

    # jogadas jogador 2

    if (jog2 == 1):
        print("segundo dado jogador")
        print(".......")
        print(".     .")
        print(".  .  .")
        print(".     .")
        print(".......")
    if (jog2 == 2):
        print("segundo dado jogador")
        print(".......")
        print("..    .")
        print(".     .")
        print(".    ..")
        print(".......")
    if (jog2 == 3):
        print("segundo dado jogador")
        print(".......")
        print("..    .")
        print(".  .  .")
        print(".    ..")
        print(".......")
    if (jog2 == 4):
        print("segundo dado jogador")
        print(".......")
        print("..   ..")
        print(".     .")
        print("..   ..")
        print(".......")
    if (jog2 == 5):
        print("segundo dado jogador")
        print(".......")
        print("..   ..")
        print(".  .  .")
        print("..   ..")
        print(".......")
    if (jog2 == 6):
        print("segundo dado jogador")
        print(".......")
        print("..   ..")
        print("..   ..")
        print("..   ..")
        print(".......")

    # comp 1

    if (comp1 == 1):
        print("primeiro dado computador")
        print(".......")
        print(".     .")
        print(".  .  .")
        print(".     .")
        print(".......")
    if (comp1 == 2):
        print("primeiro dado computador")
        print(".......")
        print("..    .")
        print(".     .")
        print(".    ..")
        print(".......")
    if (comp1 == 3):
        print("primeiro dado computador")
        print(".......")
        print("..    .")
        print(".  .  .")
        print(".    ..")
        print(".......")
    if (comp1 == 4):
        print("primeiro dado computador")
        print(".......")
        print("..   ..")
        print(".     .")
        print("..   ..")
        print(".......")
    if (comp1 == 5):
        print("primeiro dado computador")
        print(".......")
        print("..   ..")
        print(".  .  .")
        print("..   ..")
        print(".......")
    if (comp1 == 6):
        print("primeiro dado computador")
        print(".......")
        print("..   ..")
        print("..   ..")
        print("..   ..")
        print(".......")

    # comp 2

    if (comp2 == 1):
        print("segundo dado computador")
        print(".......")
        print(".     .")
        print(".  .  .")
        print(".     .")
        print(".......")
    if (comp2 == 2):
        print("segundo dado computador")
        print(".......")
        print("..    .")
        print(".     .")
        print(".    ..")
        print(".......")
    if (comp2 == 3):
        print("segundo dado computador")
        print(".......")
        print("..    .")
        print(".  .  .")
        print(".    ..")
        print(".......")
    if (comp2 == 4):
        print("segundo dado computador")
        print(".......")
        print("..   ..")
        print(".     .")
        print("..   ..")
        print(".......")
    if (comp2 == 5):
        print("segundo dado computador")
        print(".......")
        print("..   ..")
        print(".  .  .")
        print("..   ..")
        print(".......")
    if (comp2 == 6):
        print("segundo dado computador")
        print(".......")
        print("..   ..")
        print("..   ..")
        print("..   ..")
        print(".......")

    # fim do codigo
    if (jog1 + jog2) > (comp1 + comp2):
        print("Jogador Ganhou!")
        ptj = ptj + 1
        partidas = partidas + 1
        print("Jogador Venceu {} vezes".format(ptj))
    elif (comp1 + comp2) > (jog1 + jog2):
        print("Computador Ganhou!")
        ptc = ptc + 1
        partidas = partidas + 1
        print("Computador Venceu {} vezes".format(ptc))
    else:
        print("Empate!")
        ptc = 0
        ptj = 0
        ept = ept + 1
        partidas = partidas + 1
        print("houverão {} empates até agora, recomeçar os jogos".format(ptc))
print("houverão {} partidas ate o fim da disputa".format(partidas))
print("houverão {} empates ate o fim da disputa reiniciando a contagem de ambos os jogadores".format(ptc))

if ptj == 3:

    print("O jogador venceu a disputa com {} vitorias ".format(ptj))
    print("O computador perdeu a disputa com {} vitorias".format(ptc))
elif ptc == 3:
    print("O computador venceu a disputa com {} vitorias ".format(ptc))
    print("O jogador erdeu a disputa com {} vitorias".format(ptj))

print("Fim do Jogo!")
