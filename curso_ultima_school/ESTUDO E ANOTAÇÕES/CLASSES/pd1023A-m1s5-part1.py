#Estrutura de uma classe
"""class Exemplo:
    #Construtor: inicializa informações do meu objeto.
    def __init__(self):
        print("Foi criado um objeto desta classe!")
variavel = Exemplo() #Instância de um objeto da classe."""

#Como funciona o armazenamento e alteração de informações da classe
class Produto:
    def __init__(self, descricao=None, preco=None):
        #Atributos == Variáveis da classe: Atributos representam as características do objeto.
        self.descricao = descricao
        self.preco = preco
    
    def cadastrar_produto(self):
        self.descricao = input("Digite o produto atual: ")
        self.preco = float(input("Digite o preço do produto: "))
    
    def mostrar_dados(self):
        print(f"Descrição: {self.descricao}")
        print(f"Preço: R${self.preco}")
    
    def atualizar_dados(self):
        self.cadastrar_produto()
    
    def __str__(self): #Verificar
        return "<class Produto>"

    def get_descricao(self):
        return self.descricao
    
    def set_descricao(self, nova_descricao):
        self.descricao = nova_descricao

"""
#Exemplificando a criação de objetos por parâmetro
prod1 = Produto("Iphone 15 Pro Max", 15000) #Cria o objeto
prod1.mostrar_dados() #Mostra os dados

#Exemplificando a criação de objetos por cadastro via input()
prod2 = Produto() #Cria o objeto
prod2.cadastrar_produto() #Inicializar os atributos
prod2.mostrar_dados() #Mostra os dados
"""

#Adicionar informação no meu estoque
estoque = []
while True:
    print("\n1) Cadastrar, 2) Mostrar, 3) Alterar, 0) Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("----- Cadastro de Produto -----")
        produto = Produto()
        produto.cadastrar_produto()
        estoque.append(produto)
    elif opcao == 2:
        #Explorar o conteúdo do estoque
        print("----- Dados Recuperados -----")
        for id,produto in enumerate(estoque):
            print(f"----> Produto {id}")
            produto.mostrar_dados()
    elif opcao == 3:
        #Mostra os Produtos
        for id, produto in enumerate(estoque):
            print(f"----> Produto {id}: {produto.descricao}")
        id = int(input("Digite o ID do produto a ser modificado: "))
        produto = estoque[id]
        produto.atualizar_dados()
    elif opcao == 0:
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida!")