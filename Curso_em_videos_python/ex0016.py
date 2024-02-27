dias = int(input('Quantos dias de uso?'))
km = float(input('Quantos km percorridos?'))
d = dias*60
k = km*0.15
print('O valor a pagar e de: R${:.2f}'.format(d+k))

