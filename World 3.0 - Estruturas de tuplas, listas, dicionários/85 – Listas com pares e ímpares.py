print('Listas com pares e ímpares:')
valores = [[], []]
valor = 0
for v in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
        valores[0].sort()
    else:
        valores[1].append(valor)
        valores[1].sort()
print('-'*40)
print(f'Lista dos Valores: {valores}')
print('-'*40)
print(f'Os valores pares digitados: {valores[0]}')
print(f'Os valores ímpares digitados: {valores[1]}')