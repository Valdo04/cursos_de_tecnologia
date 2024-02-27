from random import randint
from time import sleep

numero = randint(0, 5)
print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. tente adivinhar....')
print('-=-' * 20)
chute = int(input('Digite seu numero da sorte !!!!'  ))
print('PROCESSANDO....')
sleep(3)
if numero == chute:
    print('----------Parabens Você acertou !!!!!!----------')
else:
    print('NÃO FOI DESSA VEZ TENTE DE NOVO')
    print('O número era {}'.format(numero))

