# Crie um programa que leia nome, ano de nascimento ecarteira de trabalho
# E cadastre-os (com idade) em um dicionário se por acaso o CTPS
# for diferente de zero, o dicionaário receberá também o ano de contratação eo salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
####################################################################################
from datetime import datetime
ano = datetime.now().year
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
   dados['Trabalho'] = int(input('Ano de Contratação: '))
   dados['Salario'] = float(input('Sálario: '))
   dados['aposentadoria'] = dados['Idade'] + ((dados['Trabalho'] + 35) - datetime.now().year)
   print(f'- nome tem o valor {dados["Nome"]}')
   print(f'- idade tem o valor {(ano - nasc )}')
   print(f'- ctps tem o valor {dados["ctps"]}')
   print(f'- Contratação tem o valor {dados["Trabalho"]}')
   print(f'- Salário tem o valor {dados["Salario"]}')
   print(f'- {dados["aposentadoria"]}')
else:
  
    print(f'- nome tem o valor {dados["Nome"]}')
    print(f'- idade tem o valor {(ano - dados["Idade"] )}')
    print(f'- ctps tem o valor {dados["ctps"]}')

print('-='*30)
print(ano - dados['Idade'])