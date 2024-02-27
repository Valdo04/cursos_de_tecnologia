
import requests

print('Usando a API fo Github\n')

usuario = input('Qual é o nome do usuário que deseja procurar ?')

url = f'https://api.github.com/users/{usuario}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f'\n nome do usuário: {data["name"]}')
    print(f'\n Bio do usuário: {data["bio"]}')
    print(f'\n Localização do usuário: {data["location"]}')
    print(f'\n Email do usuário: {data["email"]}')
else:
    print('Usuario não encontrado')