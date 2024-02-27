# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
########################################################################################

numero = int(input('Digite o numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='' )
print(f'\n\033[m O número {numero} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')