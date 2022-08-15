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
        