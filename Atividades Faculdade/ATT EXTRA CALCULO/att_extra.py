# import numpy as np
from numpy import*
# import sympy as sy
# import matplotlib.pyplot as plt

# x = sy.symbol('x')
# x = np.arange(1, 11)
# print(x)


# plt.plot(x, 2*x, color='#17a589', label='f(x) = 2x') # green
# plt.plot(x, x/2, color='red', label='f(x) = x/2')
# plt.plot(x, x+3, color='#f4d03f', label='f(x) = x + 3') # yellow



def verifica_tvm(valora, valorb, equacao=str):

    #calculando o ponto medio:
    
    equacaoa = equacao
    equacaoa = equacaoa.replace("x", (str(valora)))
    equacaob = equacao
    equacaob = equacaob.replace("x", (str(valorb)))

    funa = float(eval(equacaoa))
    funb = float(eval(equacaob))
    dervmed = (funb - funa)/(valorb - valora)

    constn = (valorb - valora) * 1000
    listax = linspace((valora + 0.001), (valorb - 0.001), num=constn)
    #para todo x dentro da lista
    equacaofor = equacao
    for xs in listax:  
    
        equacaofor = equacaofor.replace("x", (str(xs)))

        result = float(eval(equacaofor))
        if result == dervmed:
            print(result)
        else:     
            equacaofor = equacao

verifica_tvm(2, 5, "x**(1/2)")
