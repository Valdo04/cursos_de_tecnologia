#Reinventado a roda: desenvolvendo minha função "na mão"
def potencia(valor, expoente):
    resultado = valor
    for i in range(expoente-1):
        resultado = resultado * valor #É equivalente a: resultado *= valor
    return resultado

print("Resultado:", potencia(2, 5))

#Parte 1: Importando bibliotecas "default" do Python
import math
print("Resultado:", math.pow(2, 5))


#Parte 2: instalar bibliotecas
import numpy
print("Média:", numpy.mean([1,2,3,4,5]))


#Parte 3: criando minha própria biblioteca de funções
"""import minha_biblioteca

if minha_biblioteca.autentica_usuario("senha123", "senha123"):
    print("Login realizado!")
else:
    print("Senha incorreta!")"""

"""from minha_biblioteca import *

if autentica_usuario("senha123", "senha123"):
    print("Login realizado!")
else:
    print("Senha incorreta!")"""