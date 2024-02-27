

# Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa. O valor da casa,
# o sálario do comprador e em quantos anos ela vai pagar.
# calcule o valor da prestação mensal, sabendo que ela não pode excerder 30 % do sálario ou então o 
# emprestimo será negado.


############################################################################################################################


valor_casa = float(input('\033[37;1m Digite o valor da casa:\033[m '))
renda = float(input('\033[37;1m Digite o valor da sua renda:\033[m '))
tempo = int(input('\033[37;1m Digite quantos anos você que pagar:\033[m'))

valor_prestaçao = valor_casa / (tempo * 12)
renda = (renda * 30) / 100

if valor_prestaçao <= renda:
    print('\033[34;1m O emprestimo foi aprovado!!\033[m')
else:
    print('\033[31;1m O emprestimo foi negado\n sua renda não e o suficiente!!\033[m')


