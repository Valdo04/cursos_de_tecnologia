# Crie um programa que ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os 
# valores par e os valores impar digitados respectivamente
# Ao final mostre o conteúdo das três listas geradas.
##############################################################################################

valor = []
par   = []
impar = []

while True:
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]')).strip().upper()
    if resp == 'N':
        break

for num in valor:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'A lista de números é {valor}')
print(f'A lista de números pares é {par}')
print(f'A lista de números impar é{impar}')
print('FIM...')

