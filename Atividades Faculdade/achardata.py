#resposta utilizando as bibliotecas do python

import datetime

week = ("Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo")
print(week)
print()

print("Insira sua data de nascimento por favor")
dian = int(input("Insira seu dia de nascimento: "))
mesn = int(input("Insira seu mês de nascimento: "))
anon = int(input("Insira seu ano de nascimento: "))

datan = datetime.date(anon, mesn, dian).weekday()


if datan == 5 or datan == 6:
    print(f"Você nasceu em um {week[datan]}")
else:
    print(f"Você nasceu em uma {week[datan]}")
