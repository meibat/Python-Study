def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
