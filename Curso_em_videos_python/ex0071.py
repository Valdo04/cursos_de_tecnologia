# Simular caixa eletrnico
#########################################################################################

print('='* 30)
print('{:^30}'.format('BANCO VALDO'))
print('='* 30)
valor_saque = int(input("Digite o valor que deseja sacar: "))

notas_50 = notas_20 = notas_10 = notas_5 = notas_1 = 0

while valor_saque > 0:
    if valor_saque >= 50:
        valor_saque -= 50
        notas_50 += 1
    elif valor_saque >= 20:
        valor_saque -= 20
        notas_20 += 1
    elif valor_saque >= 10:
        valor_saque -= 10
        notas_10 += 1
    elif valor_saque >= 5:
        valor_saque -= 5
        notas_5 += 1
    elif valor_saque >= 1:
        valor_saque -= 1
        notas_1 += 1

print(f"Notas de 50: {notas_50}")
print(f"Notas de 20: {notas_20}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 1: {notas_1}")
