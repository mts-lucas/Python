from random import randint

# primeira jogada


while pjpc1 == 0:

    # jogadas na diagona1
    dg1 = velha[1][1]
    # jogadas na diagona2
    dg2 = velha[1][3]
    # jogadas na diagona3
    dg3 = velha[3][1]
    # jogadas na diagona4
    dg4 = velha[3][3]

    i = randint(1, 4)

    if i == 1 and dg1 == "_":
        velha[1][1] = "0"
        pjpc1 = 1
        joga += 1
        pcjogs = 1
    elif i == 2 and dg2 == "_":
        velha[1][3] = "0"
        pjpc1 = 1
        joga += 1
        pcjogs = 1
    elif i == 3 and dg3 == "_":
        velha[3][1] = "0"
        pjpc1 = 1
        joga += 1
        pcjogs = 1
    elif i == 4 and dg4 == "_":
        velha[3][3] = "0"
        pjpc1 = 1
        joga += 1
        pcjogs = 1

# tentando jogar segunda jogada
while pjpc1 == 1 and pjpc2 == 0:

    # canto 1
    if velha[1][1] == "0" and velha[1][2] == "_" and velha[1][3] == "_":
        velha[1][3] = "0"
        joga += 1
        pjpc2 = 1
        pcjogs = 1
    elif velha[1][1] == "0" and velha[2][1] == "_" and velha[3][1] == "_":
        velha[1][3] = "0"
        joga += 1
        pjpc2 = 1
        pcjogs = 1

    # canto 2
    elif velha[1][3] == "0" and velha[1][2] == "_" and velha[1][1] == "_":
        velha[1][1] = "0"
        joga += 1
        pjpc2 = 1
        pcjogs = 1
    elif velha[1][3] == "0" and velha[2][3] == "_" and velha[3][3] == "_":
        velha[3][3] = "0"
        joga += 1
        pjpc2 = 1
        pcjogs = 1

    # canto 3
    elif velha[3][1] == "0" and velha[3][2] == "_" and velha[3][3] == "_":
        velha[3][3] = "0"
        joga += 1
        pjpc2 = 1
        pcjogs = 1
    elif velha[3][1] == "0" and velha[2][1] == "_" and velha[1][1] == "_":
        velha[3][3] = "0"
        joga += 1
        pjpc2 = 1
        pcjogs = 1

    # canto 4
    elif velha[3][3] == "0" and velha[3][2] == "_" and velha[3][1] == "_":
        velha[3][1] = "0"
        joga += 1
        pjpc2 = 1
        pcjogs = 1
    elif velha[3][3] == "0" and velha[2][3] == "_" and velha[1][3] == "_":
        velha[1][3] = "0"
        joga += 1
        pjpc2 = 1
        pcjogs = 1

# atrapalhando o jogador

# jogadas nas linhas
# linha 1

if velha[1][1] == velha[1][2] and velha[1][1] == "X" and velha[1][3] == "_":
    velha[1][3] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][2] == velha[1][3] and velha[1][2] == "X" and velha[1][1] == "_":
    velha[1][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][1] == velha[1][3] and velha[1][1] == "X" and velha[1][2] == "_":
    velha[1][2] = "0"
    joga += 1
    pcjogs = 1

# linha 2

elif velha[2][1] == velha[2][2] and velha[2][1] == "X" and velha[2][3] == "_":
    velha[2][3] = "0"
    joga += 1
    pcjogs = 1
elif velha[2][2] == velha[2][3] and velha[2][2] == "X" and velha[2][1] == "_":
    velha[2][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[2][1] == velha[2][3] and velha[2][1] == "X" and velha[2][2] == "_":
    velha[2][2] = "0"
    joga += 1
    pcjogs = 1

# Linha 3

elif velha[3][1] == velha[3][2] and velha[3][1] == "X" and velha[3][3] == "_":
    velha[3][3] = "0"
    joga += 1
    pcjogs = 1
elif velha[3][2] == velha[3][3] and velha[3][2] == "X" and velha[3][1] == "_":
    velha[3][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[3][1] == velha[3][3] and velha[3][1] == "X" and velha[3][2] == "_":
    velha[3][2] = "0"
    joga += 1
    pcjogs = 1
# jogadas nas colunas faltando linha 3

elif velha[1][1] == velha[2][1] and velha[1][1] == "X" and velha[3][1] == "_":
    velha[3][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][2] == velha[2][2] and velha[1][2] == "X" and velha[3][2] == "_":
    velha[3][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][3] == velha[2][3] and velha[1][3] == "X" and velha[3][3] == "_":
    velha[3][3] = "0"
    joga += 1
    pcjogs = 1

# jogadas nas colunas faltando linha 2

elif velha[1][1] == velha[3][1] and velha[1][1] == "X" and velha[2][1] == "_":
    velha[2][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][2] == velha[3][2] and velha[1][2] == "X" and velha[2][2] == "_":
    velha[2][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][3] == velha[3][3] and velha[1][3] == "X" and velha[2][3] == "_":
    velha[2][3] = "0"
    joga += 1
    pcjogs = 1

# jogadas nas colunas faltando linha 1

elif velha[2][1] == velha[3][1] and velha[2][1] == "X" and velha[1][1] == "_":
    velha[1][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[2][2] == velha[3][2] and velha[2][2] == "X" and velha[1][2] == "_":
    velha[1][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[2][3] == velha[3][3] and velha[2][3] == "X" and velha[1][3] == "_":
    velha[1][3] = "0"
    joga += 1
    pcjogs = 1

# jogadas nas diagonais

elif velha[1][1] == velha[2][2] and velha[1][1] == "X" and velha[3][3] == "_":
    velha[3][3] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][1] == velha[3][3] and velha[1][1] == "X" and velha[2][2] == "_":
    velha[2][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[3][3] == velha[2][2] and velha[3][3] == "X" and velha[1][1] == "_":
    velha[1][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][3] == velha[2][2] and velha[2][2] == "X" and velha[3][1] == "_":
    velha[3][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][3] == velha[3][1] and velha[1][3] == "X" and velha[2][2] == "_":
    velha[2][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[3][1] == velha[2][2] and velha[2][2] == "X" and velha[1][3] == "_":
    velha[1][3] = "0"
    joga += 1
    pcjogs = 1


# Tentando vencer

# jogadas nas linhas
# linha 1

elif velha[1][1] == velha[1][2] and velha[1][1] == "0" and velha[1][3] == "_":
    velha[1][3] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][2] == velha[1][3] and velha[1][2] == "0" and velha[1][1] == "_":
    velha[1][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][1] == velha[1][3] and velha[1][1] == "0" and velha[1][2] == "_":
    velha[1][2] = "0"
    joga += 1
    pcjogs = 1

# linha 2

elif velha[2][1] == velha[2][2] and velha[2][1] == "0" and velha[2][3] == "_":
    velha[2][3] = "0"
    joga += 1
    pcjogs = 1
elif velha[2][2] == velha[2][3] and velha[2][2] == "0" and velha[2][1] == "_":
    velha[2][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[2][1] == velha[2][3] and velha[2][1] == "0" and velha[2][2] == "_":
    velha[2][2] = "0"
    joga += 1
    pcjogs = 1

# Linha 3

elif velha[3][1] == velha[3][2] and velha[3][1] == "0" and velha[3][3] == "_":
    velha[3][3] = "0"
    joga += 1
    pcjogs = 1
elif velha[3][2] == velha[3][3] and velha[3][2] == "0" and velha[3][1] == "_":
    velha[3][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[3][1] == velha[3][3] and velha[3][1] == "0" and velha[3][2] == "_":
    velha[3][2] = "0"
    joga += 1
    pcjogs = 1

# jogadas nas colunas faltando linha 3

elif velha[1][1] == velha[2][1] and velha[1][1] == "0" and velha[3][1] == "_":
    velha[3][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][2] == velha[2][2] and velha[1][2] == "0" and velha[3][2] == "_":
    velha[3][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][3] == velha[2][3] and velha[1][3] == "0" and velha[3][3] == "_":
    velha[3][3] = "0"
    joga += 1
    pcjogs = 1

# jogadas nas colunas faltando linha 2

elif velha[1][1] == velha[3][1] and velha[1][1] == "0" and velha[2][1] == "_":
    velha[2][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][2] == velha[3][2] and velha[1][2] == "0" and velha[2][2] == "_":
    velha[2][2] = "0"
    joga += 1
elif velha[1][3] == velha[3][3] and velha[1][3] == "0" and velha[2][3] == "_":
    velha[2][3] = "0"
    joga += 1
    pcjogs = 1

# jogadas nas colunas faltando linha 1

elif velha[2][1] == velha[3][1] and velha[2][1] == "0" and velha[1][1] == "_":
    velha[1][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[2][2] == velha[3][2] and velha[2][2] == "0" and velha[1][2] == "_":
    velha[1][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[2][3] == velha[3][3] and velha[2][3] == "0" and velha[1][3] == "_":
    velha[1][3] = "0"
    joga += 1
    pcjogs = 1

# jogadas nas diagonais

elif velha[1][1] == velha[2][2] and velha[1][1] == "0" and velha[3][3] == "_":
    velha[3][3] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][1] == velha[3][3] and velha[1][1] == "0" and velha[2][2] == "_":
    velha[2][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[3][3] == velha[2][2] and velha[3][3] == "0" and velha[1][1] == "_":
    velha[1][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][3] == velha[2][2] and velha[2][2] == "0" and velha[3][1] == "_":
    velha[3][1] = "0"
    joga += 1
    pcjogs = 1
elif velha[1][3] == velha[3][1] and velha[1][3] == "0" and velha[2][2] == "_":
    velha[2][2] = "0"
    joga += 1
    pcjogs = 1
elif velha[3][1] == velha[2][2] and velha[2][2] == "0" and velha[1][3] == "_":
    velha[1][3] = "0"
    joga += 1
    pcjogs = 1

while pjpc3 == 0 and pjpc2 == 2:  # terceira jogada

    if velha[1][1] == velha[1][3] and velha[1][1] == "0" and velha[3][1] == "_":
        velha[3][1] = "0"
        joga += 1
        pjpc3 = 1
        pcjogs = 1

    elif velha[1][1] == velha[1][3] and velha[1][1] == "0" and velha[3][1] == "X":
        velha[3][3] = "0"
        joga += 1
        pjpc3 = 1
        pcjogs = 1

    elif velha[1][1] == velha[3][1] and velha[1][1] == "0" and velha[1][3] == "_":
        velha[1][3] = "0"
        joga += 1
        pjpc3 = 1
        pcjogs = 1
    elif velha[1][1] == velha[3][1] and velha[1][1] == "0" and velha[1][3] == "X":
        velha[3][3] = "0"
        joga += 1
        pjpc3 = 1
        pcjogs = 1

    elif velha[3][1] == velha[3][3] and velha[3][1] == "0" and velha[1][1] == "_":
        velha[1][1] = "0"
        joga += 1
        pjpc3 = 1
        pcjogs = 1
    elif velha[3][1] == velha[3][3] and velha[3][1] == "0" and velha[1][1] == "X":
        velha[1][3] = "0"
        joga += 1
        pjpc3 = 1
        pcjogs = 1

    elif velha[3][3] == velha[1][3] and velha[3][3] == "0" and velha[3][1] == "_":
        velha[3][1] = "0"
        joga += 1
        pjpc3 = 1
        pcjogs = 1
    elif velha[3][3] == velha[1][3] and velha[3][3] == "0" and velha[3][1] == "X":
        velha[1][1] = "0"
        joga += 1
        pjpc3 = 1
        pcjogs = 1

while joga <= 7 and not(pcganha):
    i = randint(1, 3)
    j = randint(1, 3)
    cq = velha[i-1][j-1]

    if cq == "X" or cq == "0":
        print()

    else:
        velha[i-1][j-1] = '0'
        joga += 1
        pcjogs = 1
