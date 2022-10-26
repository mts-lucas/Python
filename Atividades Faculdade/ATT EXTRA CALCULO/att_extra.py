# import numpy as np
from numpy import*

import sympy as sy
import matplotlib.pyplot as plt

def verifica_tvm(valora, valorb, equacao=str):

    # calculando o ponto medio:
    equacaoa = equacao.replace("x", (str(valora)))
    equacaob = equacao.replace("x", (str(valorb)))
    funa = float(eval(equacaoa))
    funb = float(eval(equacaob))
    ponto_medio = round(((funb - funa)/(valorb - valora)), 5)
    print(ponto_medio)

    # definindo o vetor x
    constn = (valorb - valora) * 10000
    listax = linspace(valora, valorb, num=constn)
    print(listax)

    # definindo a função derivada
    x = sy.Symbol('x')
    y = eval(equacao)
    func_derivada = str(y.diff(x))
    print(func_derivada)

    media = []
    for xs in listax:
        equacaofor = func_derivada.replace("x", (str(xs)))

        result = round((float(eval(equacaofor))), 5)
        # print(result)
        if (result - 0.0001 <= ponto_medio) and (result + 0.0001 >= ponto_medio):
            media.append(result)
            # print(result)
            break

    #gerand graficos

    xg = linspace(-15.0, 15.0)
    yg = []
    for xss in xg:
        eqy1 = eval(equacao.replace("x", (str(xss))))
        eqy = float(eqy1)
        yg.append(eqy)
    
    media = round((sum(media)/len(media)), 5)
    plt.plot([valora, funa], [valorb, funb], color='#f4d03f', label=str(media))
    plt.plot(xg, yg, color='#17a589', label='Função') # green
    plt.grid(True)
    plt.legend()
    plt.show()

verifica_tvm(2, 5, "x**(1/2)")
