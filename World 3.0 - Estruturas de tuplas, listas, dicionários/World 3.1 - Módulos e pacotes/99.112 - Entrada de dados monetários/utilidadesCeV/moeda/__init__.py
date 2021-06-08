def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Aumenta o preço de acordo com a taxa
    :param preço: valor a ser aumentado
    :param taxa: taxa de aumento
    :param formato: deixa o valor formatado em dinheiro
    :return: valor aumentado
    '''
    resultado = preço + (preço*taxa/100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preço=0, taxa=0, formato=False):
    '''
    -> Diminui o preço de acordo com a taxa
    :param preço: valor a ser diminuido
    :param taxa: taxa: taxa de diminuição
    :param formato: deixa o valor formatado em dinheiro
    :return: valor diminuido
    '''
    resultado = preço - (preço*taxa/100)
    return resultado if formato is False else moeda(resultado)


def dobro(preço=0, formato=False):
    '''
    -> Dobra o valor
    :param preço: valor a ser dobrado
    :param formato: deixa o valor formatado em dinheiro
    :return: o valor dobrado
    '''
    resultado = preço*2
    return resultado if formato is False else moeda(resultado)


def metade(preço=0, formato=False):
    '''

    :param preço: valor a ser dividido ao meio
    :param formato: deixa o valor formatado em dinheiro
    :return: valor dividido ao meio
    '''
    resultado = preço/2
    return resultado if formato is False else moeda(resultado)


def moeda(preço=0, moeda='R$'):
    '''

    :param preço: valor a ser formatado
    :param moeda: moeda a ser usada
    :return: preço formatado
    '''
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(valor=0, aumento=10, diminui=5):
    '''

    :param valor: valor principal
    :param aumento: quanto o valor deve ser aumentado
    :param diminui: quanto o valor deve ser diminuido
    :return: Resumo com o valor aumentado e diminuido
    '''
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{diminui}% de redução: \t{diminuir(valor, diminui, True)}')
    print('-' * 30)
