# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas 
# daqueles que forem pares. Se o valor valor digitado for ímpar desconsidere-o.
##########################################################################################

soma = 0
cont = 0

for numeros in range(1 , 7 ):
    num_par = int(input(f'Digite o {numeros}º valor: '))
    if num_par % 2 == 0:
        soma += num_par
        cont += 1
print(f'Você infomou {cont} número pares e a soma foi {soma}')
