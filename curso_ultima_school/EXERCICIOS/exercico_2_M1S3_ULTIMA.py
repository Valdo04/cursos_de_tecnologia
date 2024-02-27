def fatorial(numero):
    print(numero)
    if numero == 1:
        return 0
    return numero * fatorial(numero-1)

retorno = fatorial(2)
print(retorno)