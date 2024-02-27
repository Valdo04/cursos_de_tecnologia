
# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos 
# de artificio, indo de 10 até  0, com uma a pausa de 1 segundo entre eles.
###############################################################################################################3

from time import sleep
import emoji 

for fogos in range(10, -1, -1):
    sleep(1)
    print(fogos)

print('BUM BUM BUM \U0001F386')