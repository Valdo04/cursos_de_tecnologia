#  Crie um programa onde o usuario uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressão passada esta com os parenteses 
# aberto e fechados na ordem correta. 
#############################################################################################
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')