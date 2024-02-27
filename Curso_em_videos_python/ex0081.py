# Crie um programa que vai ler varios numeros e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos numeros foram digitados.
# B) A lista de valores ordenada de forma decrecente 
#C) Se o valor cinco foi digitado e esta ou não na lista
#############################################################################################

valor = list()

while True:
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    valor.sort(reverse=True)
    if resp in'N':
        break
if 5 in valor:
    print(f'O valor 5 aparceu na {valor.index(5)}º posição da lidta')
else:
    print(' O valor 5 não foi digitado em nenhuma posição')
   
print(f'Os números digitados foram {valor}',end=' ')
print(f'\nForam digitado o total de {len(valor)} numero(s)')
print('FIM...')