# Crie um programa que leia duas notas de aluno e calcule sua média, mostrando uma mensagem no final, de acordo 
# com a média atigida:
# media abaixo de 5.0: reprovado
# média entre 5.0 e 6.9: recuperação
# média 7.0 ou superio : aprovado

###############################################################################################################

primeira_nota = float(input('\033[33;40m Digite sua primeira nota: \033[m'))
segunda_nota = float(input('\033[32;40m Digite sua segunda nota: \033[m'))

resultado = (primeira_nota + segunda_nota) / 2
 
if resultado < 5:
    print('\033[31;40m REPROVADO!!! \033[m')
elif resultado >= 5 and resultado <= 6.9:
    print('\033[33;40;1m RECUPERAÇÃO \033[m')
else:
    print('\033[32;40m APROVADO \033[m')


print('sua media foi',resultado)