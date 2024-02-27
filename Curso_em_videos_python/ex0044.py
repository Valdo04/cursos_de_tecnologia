# Elabore um programa que calcule um valor a ser pago pelo um produto, cosiderando seu preço normal
# e condição de pagamento:
# Á vista dinheiro/cheque: 10 % de desconto
# Á vista no cartão: 5 % de desconto
# em até 2x no cartão: preço normal 
# 3x ou mais no cartão: 20 % de juros 
###################################################################################################################

print ('{:=^40}'.format('LOJAS VADOLINO'))
produto = float(input('\033[33m Digite o valor do produto:  \033[m' ))
condiçao = str(input('\033[32m Digite a condição de pagamento:   ' )).lower()
if condiçao == 'cartão' or condiçao == 'cartao' or condiçao =='credito':
    forma_pagamento = str(input('debito ou credito?  ')).lower()
    if forma_pagamento == 'credito':
       parcela = int(input('Quantas vezes?'  )) 
       if parcela <= 2:
           print(f'O valor a pagar é R$ {produto}')
       elif parcela >= 3:
           print(f'Juros de 20% o valor a pagar será R$ {(produto / 100 * 20)+(produto)}')
    elif forma_pagamento == 'debito':
        print(f'Você teve 5% de desconto o valor a pagar será R$ {(produto / 100 * -5)+(produto)}')
elif condiçao == 'dinheiro' or condiçao == 'cheque':
    print(f'Você teve 10% de desconto o valor a pagar será R$ {(produto / 100 * -10)+(produto)}')
print('\033[32;40m OBRIGADO PELA COMPRA VOLTE SEMPRE!!! \033[m')
    



