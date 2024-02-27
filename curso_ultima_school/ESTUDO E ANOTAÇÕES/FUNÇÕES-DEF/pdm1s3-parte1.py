#Funções e Pacotes
"""def boas_vindas():
    nome = input("Digite o seu nome: ")
    print(f"Seja bem-vind@, {nome}!")

boas_vindas() #Chamada da função"""

#Exemplo de chamada de função: uma função só é executada quando chamada explicitamente!
"""def bom_dia():
    print("Bom dia!")

def boa_tarde():
    print("Boa tarde!")

def boa_noite():
    print("Boa noite!")

bom_dia()"""

#Escopo de variáveis
"""def exemplo(nome): #Escopo LOCAL
    global sobrenome #Escopo global
    sobrenome = "Lopes"
    print(f"Entrou na função: {nome} {sobrenome}")

nome = "Sherlon"      #Definição GLOBAL
sobrenome = "Almeida" #Definição GLOBAL
print("Antes da função:", nome, sobrenome)
exemplo(nome)
print("Depois da função:", nome, sobrenome)"""

#Exemplo SEM FUNÇÕES
"""for i in range(3):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu CPF: ")
    endereco = input("Digite seu Endereço: ")
    print(f"Seja bem-vind@, {nome}!")
    print(f"--- Idade: {idade}")
    print(f"--- CPF: {cpf}")
    print(f"--- Endereco: {endereco}")"""

#Exemplo COM FUNÇÕES

""" Descrição: apresenta na tela os dados do usuário de maneira formatada.
    Parâmetros:
        name -> contém o nome do usuário
        age -> contém a idade do usuário
        id -> contém o CPF do usuário
        address -> contém o Endereço do usuário
    Retorno:
        Não se aplica
"""
def mostra_dados_usuario(name, age, id, address):
    print(f"Seja bem-vind@, {name}!")
    print(f"--- Idade: {age}")
    print(f"--- CPF: {id}")
    print(f"--- Endereco: {address}")

"""Descrição: obtém dados do usuário da entrada, usando o comando input()
    Parâmetros:
        Não se aplica
    Retorno:
        Retorna os dados do usuário: nome, idade, cpf, endereco"""
def cadastro_usuario():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu CPF: ")
    endereco = input("Digite seu Endereço: ")
    return nome, idade, cpf, endereco

"""for i in range(3):
    nome, idade, cpf, endereco = cadastro_usuario()
    mostra_dados_usuario(nome, idade, cpf, endereco) #Chamada da função"""

#Versão 1
"""def soma():
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))
    print(f"Soma: {x+y}")"""

#Exemplo2
"""def soma(a, b):
    resultado = a + b
    print(f"Soma: {resultado}")
    return resultado

preco1 = float(input("Digite o preco do produto: "))
preco2 = float(input("Digite o preco do produto: "))

resultado1 = soma(preco1, preco2)
resultado2 = soma(9.5, 4.7)
print("Valores finais: ", resultado1, resultado2)"""



#Exemplo Carrinho de compras DINÂMICO

def cadastro_produto():
    global total,produtos
    nome = input("Descreva o produto: ")
    preco_produto = float(input("Digite o preco do produto: "))
    total += preco_produto
    
    produto_atual = {"nome": nome, "preco": preco_produto}
    produtos.append(produto_atual)

def atribui_desconto():
    global total
    desconto = float(input("Digite o desconto: "))
    total -= desconto

def apresenta_valor_carrinho_compras(valor_a_ser_pago):
    print(f"Valor parcial: {valor_a_ser_pago}")

def apresenta_produtos_no_carrinho(meu_carrinho):
    for produto in meu_carrinho:
        print(f"Produto: {produto['nome']} -> Preço: R${produto['preco']}")

def apresenta_menu():
    print("""
1) Cadastrar novo produto,
2) Desconto,
3) Apresenta valor a ser pago,
4) Listar produtos no carrinho,
0) Finalizar""")

produtos = [] #Armazena produtos
total = 0.0 #Valor a ser pago
while True:
    apresenta_menu()
    opcao = int(input("Digite a opcao desejada: "))

    if opcao == 0:
        print("Programa finalizado!")
        break #Finaliza um Loop
    elif opcao == 1:
        cadastro_produto()
    elif opcao == 2:
        atribui_desconto()
    elif opcao == 3:
        apresenta_valor_carrinho_compras(total)
    elif opcao == 4:
        apresenta_produtos_no_carrinho(produtos)
    else:
        print("Opção inválida!")
