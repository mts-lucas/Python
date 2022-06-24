from math import log

# print("Segunda avaliação\n")
# print("Questão 2\n")
# print("Calculo do quadrado de um numero")
# j = int(input("Por favor insira um numero: "))
# soma = 0
# for k in range(1, (j + 1)):
#     soma += (2 * k) - 1
# print(f"O quadrado de {j} é {soma}")


print("Questão 3\n")
print("Calculo da idade do seu cachorro\n")
print("Insira a idade de seu pet em anos e meses")
anos = float(input("Anos: "))
meses = float(input("Meses: "))
idade = anos + (meses/12)
idadeh = (16*(log(idade))) + 31
idadefa = int(idadeh)
idadefm = round((idadeh - (int(idadeh))) * 12)
if idadefm > 0:
    print(f"A idade humana do seu pet é aproximadamente {idadefa} anos e {idadefm} meses ")
else:
    print(f"A idade humana do seu pet é aproximadamente {idadefa} anos")