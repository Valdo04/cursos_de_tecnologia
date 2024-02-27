from random import randint

numero = randint(1, 2)

chute = int(input('Digite seu chute:  '))

if chute == numero:
     print('Parabéns você acertou')
elif chute < numero:
     print('Você errou o número era maior!')
else:
     print('Não foi dessa vez, o numero era:  ',numero)

print('FIM DO JOGO')
