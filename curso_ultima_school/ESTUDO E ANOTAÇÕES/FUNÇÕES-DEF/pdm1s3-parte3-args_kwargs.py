#Sem args
"""def soma_n_numeros(valores):
    total = 0.0
    for valor in valores:
        total += valor
    return total

precos = [1,1,1,1]
print("Resultado:", soma_n_numeros(precos))"""

#Com args
def soma_n_numeros_com_args(*args):
    print(type(args))

def soma_n_numeros_sem_args(valores):
    print(type(valores))

soma_n_numeros_com_args(2, 4, 6)
valores = (2, 4, 6)
soma_n_numeros_com_args(valores)


#Com kwargs
def com_kwargs(**kwargs):
    print(kwargs, type(kwargs))

def sem_kwargs(valores):
    print(type(valores))

com_kwargs(nome="Sherlon", idade=28)
meus_dados = {'nome': 'Sherlon', 'idade': 28}
sem_kwargs(meus_dados)