# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
# Ex: escreva('Olá, Mundo!')
# saida:
# ~~~~~~~~~~~~~~~~~~~~~
#     Olá, Mundo!
# ~~~~~~~~~~~~~~~~~~~~~~
####################################################################################################################
def escreva(txt):
    print('~'*(len(txt)+ 4))
    print(f'  {txt}')
    print('~'*(len(txt)+ 4))


escreva('Ola, Mundo!')
escreva('Vamos estudar mais um pouco, para adiquir cada vez mais conhecimento')