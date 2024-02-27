from random import randint

numero = randint(1, 2)

chute = int(input('Digite seu chute:  '))

if chute == numero:
     print('Parabéns você acertou')
else:
     print('Não foi dessa vez, o numero era:  ',numero)

print('FIM DO JOGO')
