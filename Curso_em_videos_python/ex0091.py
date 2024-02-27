# Crie um programa onde 4 jogadores joguem um dado e tenha resultads aleatorios
# Guarde esses resultados em um dicionario.No final, coloque esse dicionario
# em ordem sabendo que o vencedor tirou o maior número na rodada.
#################################################################################
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('   ==RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar {v[0]} com {v[1]}.')
