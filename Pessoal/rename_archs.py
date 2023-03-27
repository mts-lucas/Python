import os

programa_ativo = True

while programa_ativo:

    os.system('cls')
    diretorio = str(input(
        'Insira o caminho absoluto do seu diretorio:\n'))     # noqa: E501

    prefixo = str(
        input('Insira o nome que deseja dar aos seus arquivos:\n'))
    prefixo = prefixo.replace(" ", "_")
    contador = 1

    print('sua lista de arquivos renomeados:\n')

    for nome_arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, nome_arquivo)):
            nome, extensao = os.path.splitext(nome_arquivo)
            novo_nome_arquivo = f'{prefixo}_{contador}{extensao}'
            os.rename(os.path.join(diretorio, nome_arquivo),
                      os.path.join(diretorio, novo_nome_arquivo))

            contador += 1
            print(novo_nome_arquivo)

    parar = str(input('Deseja fechar o programa(s/n):\n'))
    if parar == 's' or parar == 'S':
        programa_ativo = False
