# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em 
#uma lista única que mantenha separados os valores pares e impar.No final, mostre os valores 
# pares e impares em ordem crescente
#######################################################################################################
num = [[],[]]
valor = 0
for cont in range(7):
    valor = (int(input(f'Digite o {cont+1}º valor: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort
num[1].sort
print(f'Os valores pares foram: {num[1]}')        
print(f'Os valores impar foram: {num[2]}')
