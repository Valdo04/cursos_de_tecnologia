# Crie um programa que leia varios numeros inteiros pelo teclado
# O programa só vai para quando o usuario digitar o valor 999 que é a condição de parada
# No final mostre quantos números foram digitados e qual foi a soma entre eles 
# desconsiderando o flag.
#########################################################################################################3

n = 1
cont = 0
list = []
while n != 0 :
    num = int(input('Digite um numero: '))
    list.append(num)
    cont += 1
    if num != 999:
        soma = 0 
        i = 0
        while i < len(list):
            soma += list[i]
            i += 1   
    if num == 999:
        break
print(soma)
print(f'Foram digitado o total de {cont} numeros')