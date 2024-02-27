# Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pessoas ainda nao atigiram a maioridade e quantas já são maiores.
#######################################################################################################
from datetime import date
ano = date.today().year
menor = 0
maior = 0
for n in range(1, 8):
    idade = int(input(f'Em que ano a {n}º nasceu? '))
    if ano - idade < 21:
        menor += 1
    else:
        maior += 1
print(f'Tivemos {maior} pessoas maiores de idade')
print(f'Tivemos {menor} pessoas menores de idade.')

    


