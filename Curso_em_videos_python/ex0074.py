# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre o listagem de números gerados e também indique o menor eo
# maior valor que estão na tupla.
######################################################################################
from random import randint

cont = maior = 0
menor = 6
while cont <= 4:
    num = (randint(0,5))
    cont += 1
    if num > maior:
       maior = num
    if num < menor:
       menor = num

    print(num, end=' ') 
print('')
print(f'O maior valor sorteado {maior}')
print(f'O menor valor sorteado {menor}')
