# Faça um programa qu mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# peço usuário. O programa será interrompido quando o número solicitado for negativo.
#########################################################################################
while True:
    num = int(input('que ver a tabuada de qual valor: '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!!')
    
 