#Classe mãe (MAIS GENÉRICA): contém apenas os dados definidos nela mesma
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def mostra_dados(self):
        print("Essa é a função da classe MÃE: ")
        print(f"Nome: {self.nome}")

#Classe filha (MAIS ESPECÍFICA): contém os seus próprios dados (atributos + métodos) e TAMBÉM os da classe MÃE
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        self.patas = 4
        self.som = "Au au"
        self.mostra_dados()
    
    def mostra_dados(self):
        super().mostra_dados()
        print("Essa é a função da classe FILHA: ")
        print(f"Patas: {self.patas}")
        print(f"Som: {self.som}")

#pet1 = Cachorro("ScoobyDoo")
#print(pet1.nome)

#Exemplo Personagem
class Jogador:
    def __init__(self):
        self.numero_camiseta = None
        self.nome = None
        self.ataque = None
        self.defesa = None
    
    #Tarefa: Definam os métodos do jogador
    def cadastro(self):
        pass

class Atacante(Jogador):
    def __init__(self):
        self.ataque = 100
        self.defesa = 90

class Goleiro(Jogador):
    def __init__(self):
        self.ataque = 50
        self.defesa = 100

#Podem instanciar alguns objetos das classes acima.
Time = []
numero_jogadores = 11
for i in range(numero_jogadores):
    jogador = Jogador()
    jogador.cadastro()
    Time.append()

#Apresentem na tela os 11 jogadores escalados/cadastrados.