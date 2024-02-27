# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F"
# Caso esteja errado, peça a digitação novamente até um valor correto.

##############################################################################################3


sexo = ''
while 'f' not in sexo and 'm' not in sexo:
  sexo = str(input('Digite seu sexo:[M/F]')).strip().lower()
  if sexo != 'f' and sexo != 'm':
    print('DIGITE NOVAMENTE')
print( 'VALIDO')

 


