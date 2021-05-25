import moeda, formatado
p = float(input('Digite o preço: '))
print(f'A metade de {formatado.moeda(p)} é {formatado.moeda(moeda.metade(p))}')
print(f'O dobro de {formatado.moeda(p)} é {formatado.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {formatado.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 30%, temos {formatado.moeda(moeda.diminuir(p, 30))}')