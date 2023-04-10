def reverseString(text):
    textList = list(str(text))
    newText = ""

    for i in range(len(textList), 0, -1):
        newText += textList[i-1]

    print(newText)


reverseString("Processo Seletivo 2023")
