print('{:-^40}'.format('\033[1;31mCALCULADORA\033[m'))
while True:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print('{}#-{}'.format('\033[1m','\033[m')*12)
    print('''{}Selecione um operador:
    [+] Para adição;
    [-] Para subtração;
    [*] Para multiplicação;
    [/] Para divisão{}'''.format('\033[1;32m','\033[m'))
    print('{}#-{}'.format('\033[1m','\033[m')*12)
    operador = ' '
    continuar = ' '
    while operador not in '+-*/':
        operador = str(input('Operador: '))
        if operador not in '+-*/':
            print('\033[1;31mOPÇÃO INVÁLIDA... Tente novamente:\033[m')
    if operador == '+':
        print(f'{n1} + {n2} = {n1+n2}')
    elif operador == '-':
        print(f'{n1} - {n2} = {n1-n2}')
    elif operador == '*':
        print(f'{n1} * {n2} = {n1*n2}')
    elif operador == '/':
        print(f'{n1} / {n2} = {n1/n2}')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('\033[1mPROGRAMA ENCERRADO... Até a próxima!\033[m')