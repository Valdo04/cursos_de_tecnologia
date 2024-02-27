# A confederção nacional de natação precisa de um programa que leia a data de nascimento de um atleta e mostre
# sua cagoria de acordo com sua idade:
# Até 9 anos : mirim
# Até 14 anos : infantil
# Até 19 anos: Sênior 
# Acima master
############################################################################################################################
from datetime import date
nascimento = int(input('Digite sua  data de nascimento: '))
if nascimento < 1950:
    print('\033[31;47;7m A idade digitada esta fora dos padroes\n digite sua data de nascimento com 4 numeros!!! \033[m')
ano = date.today().year

nascimento = ano - nascimento

if nascimento <= 9:
    print('MIRIM')
elif nascimento <= 14:
    print('INFANTIL')
elif nascimento <= 19:
    print('JUNIOR')
elif nascimento <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
print(nascimento)    

