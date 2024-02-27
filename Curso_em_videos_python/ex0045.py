# Crie um programa que faça o computador jogar jokenpô com você:




##################################################################################################################

from random import randint
from time import sleep

computador = randint(1,3)
print('-=-' * 20)
print('VAMOS JOGAR JOKENPÔ....')
print('-=-' * 20)

jogador = int(input(''' Escolha sua jogada
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
:    ''' ))
print('PROCESSANDO....')
sleep(2)
print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PÔ!!!')
if computador == 1: # pc jogou pedra
     if  jogador == 2:
          print('VOCÊ VENCEU PAPEL COBRE PEDRA!!!')
     elif jogador == 3:
          print('VOCÊ PERDEU PEDRA QUEBRA TESOURA!!!')
     elif computador == jogador:
          print('EMPATOU TENTE OUTRA VEZ!!!')

elif computador == 2: # pc  jogou papel
     if  jogador == 1:
          print('VOCÊ PERDEU PAPEL COBRE PEDRA!!!')
     elif jogador == 3:
          print('VOCÊ GANHOU TESOURA CORTA PAPEL')
     elif computador == jogador:
          print('EMPATOU TENTE OUTRA VEZ!!!')

elif computador == 3: # pc jogou tesoura
     if  jogador == 1:
          print('VOCÊ GANHOU PEDRA QUEBRA TESOURA')
     elif jogador == 2:
          print('VOCÊ PERDEU TESOURA CORTA PAPEL ')
     elif computador == jogador:
          print('EMPATOU TENTE OUTRA VEZ!!!')
print(computador)