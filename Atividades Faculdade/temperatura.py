from cProfile import label
import random
import matplotlib.pyplot

# temperatura madrugada
temp1 = 22
tempant1 = 22
lista_temp = []
hr = 0
lista_hr = []

for i1 in range(6):
    j1 = 0
    while j1 < 1:
        temp1 = random.uniform(22, 24)
        if (temp1 >= tempant1) and (temp1 < tempant1 + 0.5):
            tempant1 = temp1
            lista_temp.append(temp1)
            hr = hr + 1
            lista_hr.append(hr)
            j1 = 1
        else:
            j1 = 0
# temperatura manhã
temp2 = 24
tempant2 = 24

for i2 in range(6):
    j2 = 0
    while j2 < 1:
        temp2 = random.uniform(24, 30)
        if (temp2 >= tempant2) and (temp2 < tempant2 + 1.5):
            tempant2 = temp2
            lista_temp.append(temp2)
            hr = hr + 1
            lista_hr.append(hr)
            j2 = 1
        else:
            j2 = 0
# temperatura tarde
temp3 = 30
tempant3 = 30

for i3 in range(6):
    j3 = 0
    while j3 < 1:
        temp3 = random.uniform(26, 30)
        if (temp3 <= tempant3) and (temp3 > tempant3 - 2.2):
            tempant3 = temp3
            lista_temp.append(temp3)
            hr = hr + 1
            lista_hr.append(hr)
            j3 = 1
        else:
            j3 = 0

# temperatura tarde
temp4 = 26
tempant4 = 26

for i4 in range(6):
    
    j4 = 0
    while j4 < 1:
        temp4 = random.uniform(22, 26)
        if (temp4 <= tempant4) and (temp4 > tempant4 - 1.5):
            tempant4 = temp4
            lista_temp.append(temp4)
            hr = hr + 1
            lista_hr.append(hr)
            j4 = 1
        else:
            j4 = 0

tempsum = sum(lista_temp)/24
tempsumlist = []
for k in range(24):
    tempsumlist.append(tempsum)
temphora = []
temphora = lista_hr


matplotlib.pyplot.plot(lista_hr, lista_temp, label = "Temperaturas")
matplotlib.pyplot.plot(temphora, tempsumlist, label = "Temperatura Média")
matplotlib.pyplot.ylim(20.00, 30.00)
matplotlib.pyplot.xlim(0, 25)
matplotlib.pyplot.title('Temperaturas durante o dia')
matplotlib.pyplot.xlabel('Horas')
matplotlib.pyplot.ylabel('Temperatura')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()


