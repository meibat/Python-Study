from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
cont = 1
for k, v in jogadores.items():
    print(f'{k} tirou: {v} no dado.')
    sleep(1)
print('\033[1;33m-'*30)
print(f'{"RANKING":^30}')
print('-'*30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# o ranking é o dicionário transformado em lista
for k, v in ranking:
    print(f'\033[m{cont}° LUGAR: {k} com {v}.')
    cont += 1
    sleep(1)
print('FINALIZANDO PROGRAMA...')
