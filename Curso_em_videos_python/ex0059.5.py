n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2 
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} X {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'{n1} e {n2} o maior valor é {maior} ')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro numero'))
        n2 = int(input('Segundo numero'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opeção inválida. Tente novamente')
    print('=-= '* 10)
print('Fim do programa! volte aempre!')

