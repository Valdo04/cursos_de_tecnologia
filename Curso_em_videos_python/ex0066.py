# Crie um programa que leia vários números inteiros pelo teclaodo. O programa só vai para de digitar
# quando o  usuário digitar o valor 999, que é a condição de parada. No final mostre qunatos 
# números foram digitados e qual foi a soma entre eles desconsiderando o flag
#######################################################################################################

cont = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foram {soma}!')

