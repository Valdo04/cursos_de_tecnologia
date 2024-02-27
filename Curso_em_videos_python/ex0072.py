# Crie um programa que tenha uma tupla totalmente prenchida com uma contagem por extenso
# de 0 até vinte.
# seu programa deverá ler um numero pelo teclado entre 0 e 20 e mostra-lo por extenso
##############################################################################################################
contangem = ('ZERO', 'UM ', 'DOIS', 'TREIS', 'QUATRO', 'CINCO', ' SEIS', 'SETE', 'OITO', 'NOVE', ' DEZ',
             'ONZE', 'DOZE', ' TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO','DEZENOVE', 'VINTE')

while True:
    num = int(input('Digite um numero de 0 a 20: '))
    if num >= 0 and num <= 20:
        break
    print('Número invalido! Tente novamente.')
print (f'Você Digitou o número {contangem[num]}')