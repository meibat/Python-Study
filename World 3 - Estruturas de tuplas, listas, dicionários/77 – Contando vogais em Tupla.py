palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\nNa palavra \033[34m{p}\033[m temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(f'\033[33m{letra.lower()}\033[m', end=' ')
