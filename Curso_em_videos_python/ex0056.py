# Desenvolva um programa que leia nome, idade sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.
#####################################################################################################
nomes_masc = []
nomes_femi = []
idade_masc = []
idade_femi = []
soma = 0
cont_id = 0

for p in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade:'))
    sexo = int(input('''Digite seu sexo:
    [ 1 ] Masculino:
    [ 2 ] Feminino:
    :'''))

    if sexo == 1:
        nomes_masc.append(nome)
        idade_masc.append(idade)
    else:
        nomes_femi.append(nome)
        idade_femi.append(idade)
    soma += idade / 4

maior_idade_f = idade_femi [0]
mais_velho =  nomes_masc [0]
maior_idade = idade_masc [0]

for i in range(len(idade_masc)):
    if idade_masc[i] > maior_idade:
        maior_idade = idade_masc[i]
        mais_velho = nomes_masc[i]


for y in range(len(idade_femi)):
    if idade_femi[y] < 20:
        cont_id += 1
        

print(f'A média de idade do grupo é {soma}')
print(f'O homem mais velho é o {mais_velho}')
print(f'{cont_id} Mulher tem menos de 20 anos')
