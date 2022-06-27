frase1 = " Programa Agenda "
frase2 = ""
fcadastro = " 1 - Cadastrar contato "
fpesquisa = " 2 - Pesquisar contato "
fatualizar = " 3 - Atualizar contato "
fapagar = " 4 - Apagar contato "
flistar = " 5 - Listar Contatos "
fsair = "  0 - Sair  "


lista_dados = []
agenda = []
esc = " "

while esc != "0":

    print()
    print(f"{frase2:#^25}")
    print(f"{frase1:#^25}")
    print(f"{frase2:#^25}")
    print(f"{fcadastro:#^25}")
    print(f"{fpesquisa:#^25}")
    print(f"{fatualizar:#^25}")
    print(f"{fapagar:#^25}")
    print(f"{flistar:#^25}")
    print(f"{fsair:#^25}")
    print()

    esc = input("\nEscolha sua opção: ")

    if esc == "1":

        print("Vamos cadastrar um novo contato")
        print()
        newname = input("Insira o nome: ")
        lista_dados.append(newname)
        newfone = input("Insira o numero de telefone: ")
        lista_dados.append(newfone)
        newemail = input("Insira o email: ")
        lista_dados.append(newemail)
        agenda.append(lista_dados)

    elif esc == "2":

        print("Consulta")
        print()
        nomeb = input("Qual o nome à buscar? ")
        achou = False
        for pessoa in agenda:

            if nomeb.upper() in pessoa[0].upper():
                achou = True
                print(f"Nome:\t {pessoa[0]} ")
                print(f"E-mail:\t {pessoa[1]} ")
                print(f"Fone:\t {pessoa[2]} ")
                print()

    elif esc == "4":

        print("\nVamos Apagar um dos seus contatos\n")
        nomeb = input("Qual o nome do contato que deseja apagar? ")
        achou = False
        cont = 0
        for pessoa in agenda:
            cont += 1

            if nomeb.upper() in pessoa[0].upper():
                achou = True
                print(f"Nome:\t {pessoa[0]} ")
                print(f"E-mail:\t {pessoa[1]} ")
                print(f"Fone:\t {pessoa[2]} ")
                print()
                delt = input("Deseja mesmo apagar esse contato?")
                if delt.upper == "SIM":
                    agenda.pop((cont - 1))

    elif esc == "5":

        print("Seus contatos")
        print()

        for p in agenda:

            print(f"Nome:\t {p[0]} ")
            print(f"E-mail:\t {p[1]} ")
            print(f"Fone:\t {p[2]} ")
            print()


# Incluir data de nascimento
# Mostrar aniversariantes do mes
