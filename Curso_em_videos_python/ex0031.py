viagem = float(input('Digite a distancia de sua viagem:  '))
viagem1 =(viagem*0.50)
viagem2 = (viagem*0.45)


if viagem <= 200:
    print('Valor da viagem é : {}'.format(viagem1))
else viagem >= 201:
    print('Valor da viagem é : {}'.format(viagem2))
