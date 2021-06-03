def leiadinheiro(msg):
    '''
    -> Lê o valor e o válida
    :param msg: valor a ser lido
    :return: Se é válido ou não
    '''
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            válido = True
    return float(entrada)
