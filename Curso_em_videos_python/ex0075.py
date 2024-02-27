# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantos vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os numeros pares
#################################################################################################
tupla = ()
cont = 0
cont2 = 0
while cont <= 3:
    num = int(input('Digite um numero: '))
    tupla += (num),
    cont += 1
    valor = 9
    valor3 = 3
    contagem = tupla.count(valor)
    if num % 2 == 0:
        cont2 += 1
    posição = tupla.index(valor3)
print(f'Você digitou os valores {tupla}')
print(f'O valor {valor} apareceu {contagem} vezes')
print(f'O valor 3 aparece na {posição - 1}º posição')
print(f'Os valores pares foram {cont2}')
