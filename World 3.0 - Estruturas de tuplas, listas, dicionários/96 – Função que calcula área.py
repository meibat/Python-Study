def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}X{comp} é de {a}m²')


# programa principal
print('Controle de Terreno:')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
