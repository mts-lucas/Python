#em orientação  objteto tentamos reproduzir objetos humanos em codigo4

#o python tem metodos especiais como o __init__

#uma função dentro de uma classe é um metdodo//self é pra receber a propria instancia

class Pessoa: #comando class para criar um molde, e por padrão é a primeira letra maiuscula
    def __init__(self,nome, idade,comendo=False, falando=False): #todos os paremetros a serem passados
        #agora tanto caso eu queira add assim ou printar um parametro especidifico da instancia eu uso desse jeito:
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já esta comendo")
            return
        elif self.falando:
            print(f"{self.nome} não pode comer falando")
            return

        print(f"{self.nome} esta comendo {alimento}")
        self.comendo = True

    def pararcomer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer')
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo")
            return

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar comendo")
            return
        elif self.falando:
            print(f"{self.nome} já esta falando")
            return
        
        print(f"{self.nome} esta falando sobre {assunto} ")
        self.falando = True

    def parardefalar(self):
        if not self.falando:
            print(f"{self.nome} não esta falando")
            return
        print(f"{self.nome} parou de falar")
        self.falando = False

pessoa1 = Pessoa("Lucas", 22)

pessoa1.comer("Batata doce")
pessoa1.pararcomer()
pessoa1.comer("Ovo")
pessoa1.falar("poo")
pessoa1.pararcomer()
pessoa1.falar("POO")
pessoa1.parardefalar()
