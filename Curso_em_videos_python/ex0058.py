# Melhore o jogo do DESAFIO 028, computador vai 'pensar' em um numero entre 0 e 10
# Só que agora o jogo vai tentar adivinhar até acerta, mostrando no final quantos palpites
# foram necessários para vencer.
##############################################################################################################

from random import randint
from time import sleep

numero = randint(0, 10)
chute = []
cont = 1
while numero != chute:
    cont += 1
    print('-=-' * 20)
    print('vou pensar em um número entre 0 e 10 tente adivinhar....')
    print('-=-' * 20)
    chute = int(input('Digite seu numero da sorte !!!!'  ))
    print('PROCESSANDO....')
    sleep(3)
    if numero == chute:
        print('----------Parabens Você acertou !!!!!!----------')
    else:
        print('NÃO FOI DESSA VEZ TENTE DE NOVO')
        print(f'Você esta na sua {cont}º tentativa')
print(f'Você teve {cont-1} tentativa, para acerta')
       


