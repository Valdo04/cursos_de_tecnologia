# Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o numero ja exista lã dentro, ele não será adicionado.
# No final, será exibidos todos os valores únicos digitados, em ordem crescente.
######################################################################################################
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar [S/N] ')).strip()
    if r in 'Mn':
        break
    print('-='*30)
    números.sort()
    print(f'Você digitou os valores {números}')
        

    