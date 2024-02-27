from random import randint
numero = randint(1, 5)
tentativas = 5
while tentativas > 0:
    chute = int(input('Digite seu chute:  '))
    if chute == numero:
        print('Parabéns você acertou')
        break
    elif chute < numero:
        print('Você errou o número era maior!')
    else:
        print('Não foi dessa vez, o numero era menor!')
    tentativas = tentativas - 1
    

print('FIM DO JOGO o numero era',numero)
