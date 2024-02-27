salario = float(input('Digite seu salario:'))
acima = (salario*10/100)+salario
abaixo =(salario*15/100)+salario
if salario > 1250:
    print('Seu novo salario é : R$ {}'.format(acima))
elif salario <= 1250:
    print('Seu novo salario é : R$ {}'.format(abaixo))

print('FIM DE CALCULO')
