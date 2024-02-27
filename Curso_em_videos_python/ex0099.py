# Faça um programa que tenha um função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
##################################################################################################################
from time import sleep
def maior(*num):
    print('-='*30)
    print(f'Analizando os valores passados')
    print(f'{"......"}',end=' ', flush=True)
    sleep(1.5)
    for i, y in enumerate(num):
        print(f'{y}', end=' ', flush=True)
        sleep(1.5)
    print(f'Foram informados {i+1} valores ao todo. ')
    print(f'O maior valor informado foi {max(num)} ')
    print('-='*30)



maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()