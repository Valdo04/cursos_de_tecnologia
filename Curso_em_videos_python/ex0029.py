
velocidade = float(input('Digite sua velocidade: '))
multa = (7)
soma = (velocidade - 80)*multa
if velocidade > 80:
    print('Você foi multado!!!\n Voce estava a km {}\n o valor da multa é R$ {}'.format(velocidade,soma))
elif velocidade < 80:
    print('Você esta dentro da velocidade!!!')

