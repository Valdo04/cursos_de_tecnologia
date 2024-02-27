'''frase = input('Digite seu nome:')
print('Seu nome em Maiusculo é :',frase.upper(),'\nSeu nome em Minusculo é:',frase.lower())
print '{}  {}'.format(frase.strip(),len(frase))'''

nome = str(input('Digite seu nomecompleto:')).strip()
print('Analisando seu nome...')
print('Seu nome em Maiusculas é {}'.format(nome.upper()))
print('Seu nome em Minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))



