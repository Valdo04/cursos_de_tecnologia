from random import randint
quantidade = int(input('Digite a quntidade de dados: '))
tipo_dado = int(input('Digite o tipo do dado: '))
repeticao = int(input('Digite quantas vezes: '))
tentativa = 1
while tentativa <= repeticao:
    quantidade_temp = 1
    while quantidade_temp <= quantidade:
        valor = randint(1, tipo_dado)
        print(valor)
        quantidade_temp = quantidade_temp + 1
    print('-------terminou reptição-------')
    tentativa = tentativa + 1
print('FIM DO PROGRAMA!')        