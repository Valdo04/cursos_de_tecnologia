# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos 
# de três e que encontram no intervalo de 1 até 500.
################################################################################

soma = 0
cont = 0
for numeros in range(1 , 500, 2):
    if numeros % 3 == 0:
        soma += numeros
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')

    
