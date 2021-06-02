def aumentar(preço=0, taxa=0, formato=False):
    resultado = preço + (preço*taxa/100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preço=0, taxa=0, formato=False):
    resultado = preço - (preço*taxa/100)
    return resultado if formato is False else moeda(resultado)


def dobro(preço=0, formato=False):
    resultado = preço*2
    return resultado if formato is False else moeda(resultado)


def metade(preço=0, formato=False):
    resultado = preço/2
    return resultado if formato is False else moeda(resultado)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(valor=0, aumento=10, diminui=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{diminui}% de redução: \t{diminuir(valor, diminui, True)}')
    print('-' * 30)
