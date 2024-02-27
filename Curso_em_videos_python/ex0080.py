# Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em lista,
# Já na posição correta de iserção (sem usar o sort()).
# Nofinal, mostre a lista ordenada na tela.
#########################################################################################################

lista = []
for c in range(0, 5):
    n = int(input('Digite uma valor: '))
    if c == 0 or n > lista[-1]:
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')

