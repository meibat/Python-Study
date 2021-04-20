valores = []
cont = ''
while True:
    valor = int(input('Digite um número: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Número repitido, não adicionado!')
    cont = str(input('Quer continuar? [S/N]'))
    if cont in 'Nn':
        break
valores.sort()
print(f'Os valores digitados foram: {valores}')