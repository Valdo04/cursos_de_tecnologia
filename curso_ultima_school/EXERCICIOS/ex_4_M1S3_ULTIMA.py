
soma = 0
numero = int(input('Digite um numero'))
while (numero != -1): # != este operador simplesmente testa se dois valores são diferentes Ex: 10 != 20 retorna true
  soma += numero
  numero = int(input('Digite outro numero'))
print(soma)