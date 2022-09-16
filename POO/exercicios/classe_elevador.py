# Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os seguintes métodos:

# Inicializar: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);

# Entrar: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);

# Sair: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);

# Subir: para subir um andar (não deve subir se já estiver no último andar);

# Descer: para descer um andar (não deve descer se já estiver no térreo);

# Obs.: Encapsular todos os atributos da classe (criar os métodos set e get).

class Elevador():
    def __init__(self):
        self.total_andares = []
        self.andar_atual = 0
        self.capacidade = 0
        self.pessoas_presentes = 0

    def inicializar(self, capacidade, total_anderes):
        for i in range (total_anderes + 1):
            self.total_andares.append(i)
        self.capacidade = capacidade

    def entrar(self):
        if self.capacidade <= self.pessoas_presentes:
            print("Não pode entrar, número maximo de pessoas no elevador")
        else:
            self.pessoas_presentes += 1

    

