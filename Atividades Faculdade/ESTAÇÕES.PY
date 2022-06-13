# Programa que leia dia e mês de uma determinada data e a localização (hemisfério)
# do usuário e determine qual a estação do ano correspondente à data.
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
localizacao = (input('Informe o hemisfério: '))
b = input('Seu ano é bissexto? ')

if localizacao == "Sul":
    if (mes == 9) and (dia >= 22):
        print('Primavera')
    elif (mes == 10) or (mes == 11):
        print('Primavera')
    elif (mes == 12) and (dia <= 21):
        print('Primavera')
    elif (mes == 12) and (dia >= 22):
        print('Verão')
    elif (mes == 1) or (mes == 2):
        print('Verão')
    elif b == 'Não' and (mes == 3) and (dia <= 21):
        print('Verão')
    elif b == 'Sim' and mes == 3 and dia <= 20:
        print('Verão')
    elif b == 'Não' and (mes == 3) and (dia >= 22):
        print('Outono')
    elif b == 'Sim' and mes == 3 and dia >= 21:
        print('Outono')
    elif (mes == 4) or (mes == 5):
        print('Outono')
    elif b == 'Não' and (mes == 6) and (dia <= 21):
        print('Outono')
    elif b == 'Sim' and mes == 6 and dia <= 20:
        print('Outono')
    elif b == 'Não' and (mes == 6) and (dia >= 22):
        print('Inverno')
    elif b == 'Sim' and mes == 6 and dia >= 21:
        print('Inverno')
    elif (mes == 7) or (mes == 8):
        print('Inverno')
    elif b == 'Não' and (mes == 9) and (dia <= 21):
        print('Inverno')
    elif b == 'Sim' and mes == 9 and dia <= 20:
        print('Inverno')

if localizacao == "Norte":
    if (mes == 9) and (dia >= 22):
        print('Outono')
    elif (mes == 10) or (mes == 11):
        print('Outono')
    elif (mes == 12) and (dia <= 21):
        print('Outono')
    elif (mes == 12) and (dia >= 22):
        print('Inverno')
    elif (mes == 1) or (mes == 2):
        print('Inverno')
    elif b == 'Não' and (mes == 3) and (dia <= 21):
        print('Inverno')
    elif b == 'Sim' and mes == 3 and dia <= 20:
        print('Inverno')
    elif b == 'Não' and (mes == 3) and (dia >= 22):
        print('Primavera')
    elif b == 'Sim' and mes == 3 and dia >= 21:
        print('Primavera')
    elif (mes == 4) or (mes == 5):
        print('Primavera')
    elif b == 'Não' and (mes == 6) and (dia <= 21):
        print('Primavera')
    elif b == 'Sim' and mes == 6 and dia <= 20:
        print('Primavera')
    elif b == 'Não' and (mes == 6) and (dia >= 22):
        print('Verão')
    elif b == 'Sim' and mes == 6 and dia >= 21:
        print('Verão')
    elif (mes == 7) or (mes == 8):
        print('Verão')
    elif b == 'Não' and (mes == 9) and (dia <= 21):
        print('Verão')
    elif b == 'Sim' and mes == 9 and dia <= 20:
        print('Verão')
