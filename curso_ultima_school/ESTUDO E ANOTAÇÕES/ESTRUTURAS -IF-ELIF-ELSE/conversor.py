def formata_romano(letra, repeticao):
    return str(letra*repeticao)
# 1 I # 2 II # 3 III # 4 IV 
def convercao(numero):
    lista = ['I', 'V', 'X']
    n1 = 'I'
    n2 = 'V'
    n3 = 'X'
    if numero <= 3:  # de 1 a 3
        return lista[0]*numero
    elif numero == 4: # 4
        return 'IV'
    elif numero >= 5 and numero <9: # de 5 a 8
        repetir =numero -5
        return 'V'+'I'*repetir
    elif numero == 9: # 9
        return 'IX'
    elif numero % 10 == 0 and int(numero/10) <= 3:
        repetir = int(numero/10)
        return formata_romano(lista[2], repetir)
    elif numero <= 13:
        return lista[2]+lista[0]*int(numero-10)
    elif numero == 14:
        return 'XIV'
    elif numero >= 15 and numero <19: # de 15 a 18
        repetir =numero -5
        return 'XV'+ lista[0]*int(numero-15)
    elif numero == 19: # 19
        return 'XIX'
    elif numero % 20 == 0 and int(numero/20) <= 3:
        repetir = int(numero/10)
####################################################################
numero = int(input('Digite o numero: '))

numero_romano = convercao(numero)
print('Numero em romano', numero_romano)
