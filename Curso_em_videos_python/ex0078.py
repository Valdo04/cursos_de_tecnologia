# Faça um progama que leia 5 valores numericos e guarde-os em uma lista.
#No final, mostre qual foi o maior eo menor valor digitado e as suas respectivas posições na lista.
#########################################################################################################

num = list()

for n in range(5):
    num.append(int(input('Digite um numero: ')))
maior = max(num)
menor = min(num)
pos_maior = num.index(maior)
pos_menor = num.index(menor)

print(f'O maior valor é {maior} é sua posição é {pos_maior}')
print(f'O menor valor é {menor} é sua posição é {pos_menor}')




