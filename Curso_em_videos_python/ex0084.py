# Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
# No final, mostre
# A) Quantas pessoas foram cadastrads.
# B) Uma listagem com as pessoas mais pesadas>
# C) Uma listagem com as pessoas mais leves.
#################################################################################################################

dados = []
geral =  []
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Qual é seu peso?')))
    if len(geral) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    geral.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]? ')).strip()
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(geral)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end='')
for p in geral:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in geral:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
        

    