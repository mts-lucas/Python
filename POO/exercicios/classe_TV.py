# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

# vou adicioar um sistema de lembrança de canal e um pra ligar e desligar a tv

class Tv:

    def __init__(self, ligada=False, canal=0, volume=0):
        self.ligada = ligada
        self.canal = canal
        self.volume = volume

    def ligar(self):
        if not self.ligada:

            self.ligada = True
            print("Tv ligada")

        else:

            print("Tv ja esta ligada...")
            return

    def desligar(self):
        if not self.ligada:
            print("Tv ja esta desligada...")
            return

        else:
            self.ligada = False
            print("Tv desligada")


    def aumentar_volume(self, valor):
        if not self.ligada:
            print("Operação indisponivel: Tv desligada")
            return

        else: 

            if valor <= 100:
                self.volume = valor 

            else:
                print("Volume muito alto")
                return 

            
    def abaixar_volume(self, valor):
        if not self.ligada:
            print("Operação indisponivel: Tv desligada")
            return

        else: 

            if valor >= 0:
                self.volume = valor 

            else:
                print("Volume muito baixo")
                return    
    

    def mudar_canal(self, novocanal):
        if not self.ligada:
            print("Operação indisponivel: Tv desligada")
            return

        else: 

            if novocanal >= 0 and novocanal <= 999:
                self.canal = novocanal 

            else:
                print("Esse canal não existe")
                return    


tv1 = Tv()
tv1.mudar_canal(12)
tv1.ligar()
tv1.mudar_canal(12)
print(tv1.canal)
tv1.ligar()


