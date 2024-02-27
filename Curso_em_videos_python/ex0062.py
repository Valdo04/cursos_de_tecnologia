# Melhore o desafio 061, perguntando para o usuario se ele que mostrar mais alguns termos
# O programa encerra quando ele disser que quer mostrar 0 termo.
###########################################################################################

print('GERADOR DE PA')
primeiro = int(input('Digite o primeiro termo:  '))
razao = int(input('Razão:  '))
termo = primeiro 
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= mais:
        print(f'{termo}', end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Gostaria de mostra mais termos? se sim quantos?'))
print(f'Progressão finalizada com {total} termos mostrado')

    


