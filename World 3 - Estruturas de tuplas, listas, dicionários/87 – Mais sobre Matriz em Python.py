print('Mais sobre matriz em python:')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
numpar = numter = maior = 0
for i in range(0, 3): #linha
    for j in range(0, 3): #coluna
        matriz[i][j] = int(input(f'Digite o primeiro número [{i},{j}]: '))
print('-'*40)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='') #matriz formatada
        #Análise dos dados coletados:
        if matriz[i][j] % 2 == 0: #soma dos pares
            numpar += matriz[i][j]
        if j == 2: # soma da terceira coluna
            numter += matriz[i][j]
        if i == 1: # maior valor da segunda linha
            if j == 0 or matriz[i][j] > maior:
                maior = matriz[i][j]
    print() #quebra a linha quando acaba o i
print('-'*40)
print(f'A soma dos valores pares é {numpar}.')
print(f'A soma dos valores da terceira coluna é {numter}.')
print(f'O maior valor da segunda coluna é {maior}.')
