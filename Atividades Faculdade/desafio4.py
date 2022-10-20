#Codigo que verifica se é seu aniversario

import datetime
print("Insira sua data de nascimento por favor\n")
dia = int(input("Insira o dia: "))
mes = int(input("Insira o mes: "))
ano = int(input("Insira o ano: "))

diav = datetime.date.today().day
mesv = datetime.date.today().month
anov = datetime.date.today().year

if (dia == diav) and (mes == mesv):
  print("Parabens! Hoje é seu aniversario, voce esta completando {} anos de idade".format((anov-ano)))
elif (mes < mesv) or (mes == mesv and dia < diav):
  print("Você tem {} anos de idade e ja aniversariou este ano".format((anov-ano))) 
else:
  print("Você tem {} anos de idade e completara {} anos este ano".format(((anov-ano)-1),(anov-ano)))