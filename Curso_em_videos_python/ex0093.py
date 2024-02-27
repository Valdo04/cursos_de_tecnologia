# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final,tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.
##############################################################################################################

dados = {}
gols = []

dados['nome'] = str(input('Nome: '))
partidas = int(input('Quantas Patirdas: '))
for n in range(0,partidas):
    gols.append(int(input(f'Gols {n+1}º Partida: ')))
    tol = sum(gols)
dados['gols'] = gols 
dados['total'] = tol
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
for i, y in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {y} gols.')
print(f'Foi um toal de {dados["total"]}')