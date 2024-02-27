# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# - Não existe valor maior, os dois são iguais 


######################################################################################################################

primeiro_numero = int(input('\033[32;1m digite o primeiro numero:  \033[m'))
segundo_numero = int(input('\033[32;1m Digite o segundo numero:   \033[m '))

if primeiro_numero > segundo_numero:
    print(f'O primeiro numero e maior {primeiro_numero}!!!')
elif segundo_numero > primeiro_numero:
    print(f'O segundo numero é maior {segundo_numero}')
else:
    print(f'Os numeros são iguais!!!!{primeiro_numero} = {segundo_numero} ')