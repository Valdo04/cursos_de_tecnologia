# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120
#################################################################################################

n = int(input('Digite um número para calcularn seu fatorial'))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f' {c} ', end='')
    print('X' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')