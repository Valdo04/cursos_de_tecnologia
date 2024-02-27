# Faça um programa que leia nome e media de um aluno
# Guardando também a situação em um dicionario. No final, mostre
# O conteudo da estrutura na tela.
####################################################################################################################

dados = {}

dados['Nome'] = str(input('Nome:'))
dados['Média']= float(input(f'Média de {dados["Nome"]}: '))
print('-~'*30)
print(f'{dados["Nome"]}')
if dados['Média'] >= 7:
    print(f'Média é igual a {dados["Média"]}')
    print('Situação é igual a "APROVADO"')
else:
    print(f'Média e igual a {dados["Média"]}')
    print('Situação é igual a "REPROVADO"')
