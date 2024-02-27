# Desenvolva uma logica que leia o peso e altura de um pessoal. calcule seu IMC e mostre seu status, de acordo 
# com a tabela a baixo :
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: obesidade morbida
#IMC = 70 (1.75 * 1.75)

#######################################################################################################################



altura = float(input('\033[33m Digite sua altura: \033[m'))
peso = float(input('\033[33m Digite seu peso: \033[m'))
imc = peso / (altura ** 2) 

if imc <= 18.5:
    print('\033[33m VOCÊ ESTÁ ABAIXO DO PESO!! \033[m')
elif imc > 18.5 and imc <= 25:
    print('\033[33m VOCÊ ESTÁ NO PESO IDEAL!!!! CONTINUE ASSIM!!! \033[m')
elif imc > 25 and imc <= 30:
    print('\033[33m VOCÊ ESTÁ COM SOBREPESO!!! \033[m')
elif imc > 30 and imc <= 40:
    print('\033[33m VOCÊ ESTÁ COM OBESIDADE!!! \033[m ')
elif imc > 40:
    print('\033[35mVOCÊ ESTÁ COM OBESIDADE MORBIDA \033[m')

print('\033[32mSEU IMC É \033[m',imc)
