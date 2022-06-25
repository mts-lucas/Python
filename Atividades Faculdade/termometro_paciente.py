print("vamos verificar a temperatura média do seu paciente durante o decorrer do dia\n")

lista_temp = []
listahr =[]

for i in range(0, 24, 3):
    
    temp = float(input(f"Por favor insira a temperatura do seu paciente as {i:0>2}:00: "))
    listahr.append(i)
    lista_temp.append(temp)

soma = 0

for j in lista_temp:
    soma += j

media = soma/(len(lista_temp))

print(f"\nA temperatura média do seu paciente foi {media:.2f}º")

counta = 0
listapassh = []

for a in listahr:

    counta += 1

    if lista_temp[(counta - 1)] > media:
        listapassh.append(a)
qt = len(listapassh)

print(f"\nSeu Paciente ultrapassou a temperatura média de {media:.2f}º {qt} vezes nos seguintes horários:\n")

for b in listapassh:
    print(f"{b:0>2}:00")

print("\nFim do programa")