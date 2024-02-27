# Crie uma tupla prenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados 
# b) Os ultimos 4 colocados da tabela
# C) uma lista com os times em ordem alfabetica 
# D) em que posição esta o time do Palmeiras
#############################################################################################################3

tabela = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR',
'Atlético-MG','Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino',
 'Coritiba', 'Cuiabá', 'Grêmio','Vasco', 'Bahia')
tabela_ordem = tuple(sorted(tabela))
posição = tabela.index('Palmeiras')
print('-'*30)
print(f'Os cinco primeiro colocado são :\n{tabela[:5]}')
print('-'*30)
print(f'Os ultimos quatro colocado na tabela são :\n {tabela[16:]}')
print('-'*30)
print(f'Ordem alfabetica:\n {tabela_ordem}')
print('-'*30)
print(f'O time do Palmeiras está na : {posição + 1}º posiçao')
