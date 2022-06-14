from random import shuffle


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
achou = False
while not achou:
    shuffle(lista)
    l1 = lista[0] + lista[1] + lista[2]
    l2 = lista[3] + lista[4] + lista[5]
    l3 = lista[6] + lista[7] + lista[8]
    c1 = lista[0] + lista[3] + lista[6]
    c2 = lista[1] + lista[4] + lista[7]
    c3 = lista[2] + lista[5] + lista[8]
    d1 = lista[0] + lista[4] + lista[8]
    d2 = lista[2] + lista[4] + lista[6]
    if l1 == 15 and l2 == 15 and l3 == 15 and c1 == 15 and c2 == 15 and c3 == 15 and d1 == 15 and d2 == 15:
        achou = True
print()
print("Quadrado Mágico")

for i in range(3):
    print('|', end='')
    for j in range(3):
        print('%3d' % lista[i*3+j], end='')
