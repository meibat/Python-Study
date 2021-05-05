def fatorial(x, show=False):
    '''
    Calcular o fatorial de um número.
    :param x: número a ser calculado.
    :param show: (opcional) mostrar a conta
    :return: resultado do fatorial.
    '''
    cont = 1
    print('-' * 40)
    for num in range(x, 0, -1):
        if show:
            print(num, end='')
            if num > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        cont *= num
    print(cont)


numero = int(input('Digite um número para ver o seu fatorial: '))
fatorial(numero, show=True)
