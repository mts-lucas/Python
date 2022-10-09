from random import randint

class Pessoa: 

    ano_atual = 2022 #variaveis criadas fora de metodos são globais para a classe, isso é um atributo de classe

    def __init__(self,nome, idade): 

 
        
        self.nome = nome
        self.idade = idade

    def get_nascimento(self): #atributo de instancia
        print(self.ano_atual - self.idade)

    @classmethod #para atribuir q esse metodo é da classe(molde) e não da instancia
    def por_ano_nascimento(cls, nome, ano_nascimento): #por convenção se usa cls para metodos de classe(Pessoa), assim como self em metodos comuns
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade) #cls chama a propria classe

    #metodos estaticos não utilizam nem a classe nema instancia, é uma função normal que precisa estar dentro da classe

    @staticmethod #atribuir que é um metodo estatico
    def gera_id():
        rand = randint(10000, 19999)
        return rand




p1 = Pessoa("Lucas", 22)

p1.get_nascimento()

p2 = Pessoa.por_ano_nascimento("Lucas", 2000)
print(p2.idade, p2.nome)
print(Pessoa.gera_id())