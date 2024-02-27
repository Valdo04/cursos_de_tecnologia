# Crie um programa que leia varios numeros inteiros pelo teclado
# No final da execução, mostre a media entre todos os valores e qual foi o
# maior e o menor valores lido. O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.
##############################################################################################

cont = soma = num = media = maior = menor = 0
frase = 'S'
while frase in 'Ss':
   num = int(input('Digite um numero: '))
   cont += 1
   soma += num
   if cont == 1:
      maior = menor = num
   else:
      if num > maior:
         maior = num
      if num < menor:
         menor = num  
   frase = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')



    
    