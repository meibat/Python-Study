print('Palpites para a Mega Sena:')
print('-'*40)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('-'*40)
from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
quant = int(input('Quantos jogos quer que eu sorteie? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=='*3, f'SORTEANDO {quant} JOGOS', '=='*3)
for i, j in enumerate(jogos):
    sleep(1)
    print(f'Sorteio {i+1}: {j}')
print('=='*6, f'BOA SORTE', '=='*6)
