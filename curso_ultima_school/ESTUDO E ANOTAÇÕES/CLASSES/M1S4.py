class Cliente:
  #Construtor (inicializa o objeto)
  def __init__(self):
    #Atributos (como variáveis)
    self.nome  = None
    self.cpf   = None
    self.idade = None
  
  #Metodo (como funções)
  def mostrar_dados(self):
    print("Cliente:", self.nome, "CPF:", self.cpf, "Idade:", self.idade)
  
  def cadastro(self):
    self.nome  = input()
    self.cpf   = input()
    self.idade = int(input())

clientes = [] #Lista de clientes

for cliente in range(5):
  cadastro_atual = Cliente() #Cria o objeto
  cadastro_atual.cadastro()  #Realiza o cadastro do cliente atual
  clientes.append(cadastro_atual) #Salva o cliente atual na lista de clientes

#Mostrando os dados dos Clientes
for cliente in clientes: 
  cliente.mostrar_dados()