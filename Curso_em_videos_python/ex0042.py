# Reforça o desafio 35 dos triângulos, acrecentando o recurso de mostra que tipo de triângulo
# será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais 
# Escaleno: todos os lados diferentes

######################################################################################################################

print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro seguimento'))
r2 = float(input('Segundo seguimento'))
r3 = float(input('Terceiro Seguimento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimentos NÃO PODEM FORMAR triângulo!')
if r1 == r2  == r3:
    print('O tipo de triângulo formado foi um EQUILÁTERO\n todos os lados são iguais ')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('O tipo de triângulo formado foi um ISÓSCELES\n dois lados são iguais ')
elif r1 != r2 and r1 != r3 and r2 != r3:
    print('O tipo de triângulo formado foi um ESCALENO\n todos os lados são diferentes ')
