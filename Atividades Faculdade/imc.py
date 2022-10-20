#calc de imc

print("Calculadora de IMC\n")
nome = input("por favor insira seu nome: ")
peso = float(input("por favor insira seu peso em Kg: "))
alt = float(input("por favor insira sua altura em mt: "))
imc = round(peso / (alt**2), 2)

if imc >= 40:
    print("Cuidado {}, seu IMC é {}".format(nome, imc))
    print("Você esta classificando como obesidade grau 3(mórbida) e está no grupo de risco")
else:
    print("{}, seu IMC é {}".format(nome, imc))
    print("você não esta no grupo de risco")
