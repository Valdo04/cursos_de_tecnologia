# Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será
# a base de conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecinal
############################################################################################################


numero = int(input('\033[31;47;1m Digite um numero:  \033[m'))
print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL'''  )
base_conver = int(input('\033[31;47;1m Sua opção: \033[m'))
if base_conver == 1:
    print(f'\033[34;1mA conversão para BINARIO é:\033[m \033[32;47;1 {bin(numero)} \033[m')
elif base_conver == 2:
    print(f'\033[34;1m A conversão para OCTAL é:\033[m \033[32;47;1 {oct(numero)}\033[m')
elif base_conver == 3:
    print(f'\033[34;1m A conversão para HEXADECINAL é:\033[m \033[32;47;1 {hex(numero)}\033[m ')
else:
    print('OPÇÃO INVALIDA TENTE NOVAMENTE')
