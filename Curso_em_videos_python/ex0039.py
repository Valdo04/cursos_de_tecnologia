# Faça uma programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no servirço militar ### < 17
# Se eé hora a hora de se alistar. = 18
# Se já passou do tempo do alistamento. > 18
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

################################################################################################################
from datetime import date
nascimento = int(input('\033[33mDigite sua idade:\033[m  ')) 
if nascimento < 1950:
    print('\033[31;47;7m A idade digitada esta fora dos padroes!!! \033[m')
ano = date.today().year
nascimento = ano - nascimento 

if nascimento == 0 or nascimento < 17:
    print(f'\033[32mVocê ainda vai se alistar no servirço militar\n Falta {18 - nascimento} anos para esta data!!\033[m')
elif nascimento == 17 or nascimento == 18:
    print('Você ja pode se alistar!!')
elif nascimento > 19 and nascimento < 50:
    print(f'Já passou do tempo de se alistar, você esta {nascimento - 18} anos atrasado!!!')

print('\n \033[40;7m sua idade è',nascimento,'anos\033[m')