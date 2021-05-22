print('Matriz em python:')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
num = 0
for i in range(0, 3): #linha
    for j in range(0, 3): #coluna
        matriz[i][j] = int(input(f'Digite o primeiro número [{i},{j}]: '))
print('-'*40)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print() #quebra a linha quando acaba o i