# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos numeros
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
#############################################################################################################


opcao = 0
while opcao != 5 :
    valor1 = float(input('Digite o primeiro numero: '))
    valor2 = float(input('Digite o segundo valor: '))
    opcao  = int(input('''ESCOLHA UMA OPÇÃO:
    [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos numeros [ 5 ] sair do programa
    :  '''))
    if opcao == 1:
        resultado1 = valor1 + valor2
        print(f'Á SOMA DOS VALORES É {resultado1}')
    if opcao == 2:
        resultado2 = valor1 * valor2
        print(f'Á SOMA DOS VALORES É {resultado2}')

    if opcao == 3 and valor1 > valor2:
        print(f'O maior valor é o valor {valor1}')
    elif opcao == 3 and valor2 > valor1:
        print(f'O maior valor é o valor {valor2}')
    if opcao == 4:
        continue
    if opcao == 5:
        print('FIM DO PROGRAMA')
        break
   

    

        