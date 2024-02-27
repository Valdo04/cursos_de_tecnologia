# Refaça o desafio 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.
##################################################################################################33

print('GERADOR DE PA')
primeiro = int(input('Digite o primeiro termo:  '))
razao = int(input('Razão:  '))
termo = primeiro 
cont = 1
while cont <= 10:
   print(f'{termo}', end=' -> ')
   termo += razao
   cont += 1

print('FIM')

