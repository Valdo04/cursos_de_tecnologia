# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será uma valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
######################################################################################################################
#def fatorial(n, show=False):

fatorial = 1
var = 0
num = int(input('digite um numero: '))
for i in range(1, num +1):
    fatorial *= i
    var = num - i
    print(f'{num} X {num -i} ', end=' ')
print()
print(fatorial)