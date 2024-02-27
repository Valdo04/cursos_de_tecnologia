# Desenvolva um programa que leia o primenro termo e a razão de um PA. no final, mostre 
# os 10 primeiros termos dessa progressão.
###################################################################################################3


n1= int(input('Digite o primeiro termo:  '))
n2 = int(input('Razão:  '))
n3 = n1 + (10 -1) * n2
for i in range(n1, n3 + n2, n2 ):
    print(f'{i}', end=' -> ')
print('FIM')
