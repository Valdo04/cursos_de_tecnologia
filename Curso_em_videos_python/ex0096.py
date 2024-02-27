# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (Largura e comprimento) e mostre área do terreno.
##############################################################################################################

def área(larg, comp):
    s = larg * comp
    print(f'A área de um terreno {a} X {b} é de {s} m²')


print('     CONTROLE DE TERRENOS')
print('-'*30)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
área(a,b)
