#n1 = int(input('digite um numero:'))
#print('seu dobro',(n1*2))
#print('seu triplo',(n1*3))
#print('sua raiz quadrada',(n1**2))

n = int(input('Digite um numero:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print(' O doblo de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
