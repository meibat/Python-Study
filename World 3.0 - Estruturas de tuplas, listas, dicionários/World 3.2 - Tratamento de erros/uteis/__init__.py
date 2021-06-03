def leiaint(msg):
    '''
    -> Tenta ler o valor
    :param msg: valor a ser lido
    :return: o valor ou indica o erro
    '''
    while True:
        try:
            n = int(input(msg))
        except(KeyboardInterrupt):
            print(f'\033[1;31mProcesso interrompido pelo usuário.\033[m')
            return 0
        except(ValueError, TypeError):
            print(f'\033[1;31mERRO: não é um número inteiro. Tente novamente!\033[m')
        else:
           return n


def leiafloat(msg):
    '''
    -> Tenta ler o valor e o válida
    :param msg: valor a ser lido
    :return: o valor ou indica o erro
    '''
    while True:
        try:
            n = str(input(msg)).strip().replace(',', '.')
            n = float(n)
        except(KeyboardInterrupt):
            print(f'\033[1;31mProcesso interrompido pelo usuário.\033[m')
            return 0
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: não é um número flutuante. Tente novamente!\033[m')
        else:
            return n