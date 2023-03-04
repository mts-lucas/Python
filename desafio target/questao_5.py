# 5) Escreva um programa que inverta os caracteres de um string.


# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer
# entrada de sua preferência
# ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;

def reverseString(text):
    textList = list(str(text))
    newText = ""

    for i in range(len(textList), 0, -1):
        newText += textList[i-1]

    print(newText)


reverseString("Processo Seletivo")
