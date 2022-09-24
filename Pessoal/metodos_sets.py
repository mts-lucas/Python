#metodos da classe set

#sets tem funcoes de conjuntos, como união

conjunto_a = {1, 2}
conjunto_b = {3, 4}

uniao = conjunto_a.union(conjunto_b)
print(conjunto_a)
print(conjunto_b)
print(uniao)

#intersecção

intersec = uniao.intersection(conjunto_b)
print(intersec)

#diferença = oq sobra do primeiro conjunto mais a intersecção

dif = uniao.difference(conjunto_b)
print(dif)

#diferança simetrica = tudo menos oq ta na intersecção

conjunto_c = {1, 2, 3, 4, 5, 6}
conjunto_d = {4, 5 ,6 , 7, 8, 9}
symdif = conjunto_c.symmetric_difference(conjunto_d)
print(symdif)

#sub-conjuntos

conjunto_a.issubset(conjunto_c)

#superconjuntos

conjunto_c.issuperset(conjunto_a)

#disjunção

conjunto_a.isdisjoint(conjunto_b)

#adicionar no conjunto caso nao exista

conjunto_a.add(7)
print(conjunto_a)

#.clear limpa o set
#.copy copia seu set
#.discard se tiver o valor na lista ele discarta se não, não faz nada
#.pop remove o primeiro item da lista
#.remove mesma coisa q discard porem se não existir da erro
#
