# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá pergunta se o usuário que ou não continuar. No final, Mostre:
# A) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados
# c) Quantas mulheres tem menos de 20 anos.
##################################################################################################3

maior_18 = 0
soma_homens = 0
soma_mulheres = 0
while True:
        print('-'*30)
        print('     CADASTRE UMA PESSOA')
        print('-'*30)    
        idade = (input('Digite sua idade: '))
        if idade.isnumeric():
            idade = int(idade)
        else:
            print('Valor invalido! tente novamente!')
            continue
        sexo = ' '
        while sexo not in 'MF':
            sexo =str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
        opção = ' '
        while opção not in 'SN':
            opção = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if idade >= 18:
            maior_18 += 1
        if sexo == 'M':
            soma_homens += 1
        if sexo  == 'F' and idade < 20:
            soma_mulheres += 1
        if opção == 'N':
            break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {soma_homens} homens cadastrados')
print(f'E temos {soma_mulheres} com menos de 20 anos')
        