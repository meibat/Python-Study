print('Validando expressões matemáticas:')
exp = str(input('Digite uma expressão: '))
pilha = []
for simb in exp:
    if simb == '(':#procura a abertura
        pilha.append('(')
    elif simb == ')':#procura a fechadura
        if len(pilha) > 0:
            pilha.pop()#remove o último elemento da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
