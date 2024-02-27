def autentica_usuario(senha_digitada, senha_real):
    if senha_digitada == senha_real:
        return True
    else:
        return False

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

#Tarefinha de casa
def atribui_desconto_porcentagem(valor, percentual_desconto):
    #Desenvolvam a lógica do percentual aqui
    return valor_atualizado_com_desconto

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