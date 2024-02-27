# Reffaça o desafio 009, mostrando a tabuada de número que o usuário 
# escolher, só que agora ultilizando um laço FOR.

#########################################################################################################

numero = int(input('Digite o numero '))
for tabuada in range(1,11):
    print(f'{numero} X {tabuada} = {numero * tabuada}')